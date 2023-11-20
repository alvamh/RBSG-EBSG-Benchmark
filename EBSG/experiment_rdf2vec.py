import sys
from rdflib.namespace import RDF, FOAF, XSD, RDFS, OWL
from rdflib import OWL, Graph, Namespace, URIRef, Literal, BNode
import owlrl
import numpy as np
from math import log
import re
from prettytable import PrettyTable
import random
from datetime import datetime, time, timedelta
import statistics as stat

from rdf2vec_function import rdf2vec_func
from score_rdf2vec import score_triples_max, score_triples_mean
from create_summary import create_summary

g = Graph() #the full graph
g_data = Graph() #graph to collect resources to create embeddings for
ent_set = set()
res_set = set()
g_data.parse("Dataset_experiment_main\mappingbased_objects_en_reduced_reduced_p.ttl")
for s, p, o in g_data.triples((None, None, None)):
    ent_set.add(s)
g_data.parse("Dataset_experiment_main\instance_types_en_reduced_reduced_p.ttl")
for s, p, o in g_data.triples((None, None, None)):
    if p == RDF.type:
        res_set.add(s)
        res_set.add(o)
    else:
        res_set.add(s)
        res_set.add(p)
        res_set.add(o)
res_set.remove(URIRef("http://www.w3.org/1999/02/22-rdf-syntax-ns#Property"))
print(len(g_data))

g.parse("Dataset_experiment_main\mappingbased_objects_en_reduced_reduced_p.ttl")
g.parse("Dataset_experiment_main\instance_types_en_reduced_reduced_p.ttl")
g.parse("Dataset_experiment_main\ontology_2015-10_reduced.ttl")
print(len(g))

ent_set = list(ent_set)
res_set = list(res_set)

def run_experiment():
    times_embedding = {} #running time for pyRDF2Vec
    times_scoring_max = {} #running time for scoring, ranking and creating a snippet with score_max
    times_scoring_mean = {} #running time for scoring, ranking and creating a snippet with score_mean

    for n in [1, 5, 10]: #signature-sizes

        times_embedding[n] = []
        times_scoring_max[n] = []
        times_scoring_mean[n] = []

        for i in range(1):
            # create signature
            sign_init = []
            sign_init.append(random.choice(ent_set))
            if n > 1:
                rest = random.choices(res_set, k=(n-1))
                for r in rest:
                    sign_init.append(r)

            print(n, i)
            for sig in sign_init:
                print(sig)

            #create the embeddings
            startTime = datetime.now()
            embeddings, r_convert_set = rdf2vec_func(g_data)
            endTime = datetime.now()
            times_embedding[n].append(endTime - startTime)

            #score triples with score_max
            startTime = datetime.now()
            scores_max = score_triples_max(r_convert_set, embeddings, g, sign_init, n)
            sum_max = create_summary(scores_max, 5)
            endTime = datetime.now()
            times_scoring_max[n].append(endTime - startTime)

            #score triples with score_mean
            startTime = datetime.now()
            scores_mean = score_triples_mean(r_convert_set, embeddings, g, sign_init, n)
            sum_mean = create_summary(scores_mean, 5)
            endTime = datetime.now()
            times_scoring_mean[n].append(endTime - startTime)

    return times_embedding, times_scoring_max, times_scoring_mean

def print_table(times):
    t = PrettyTable()
    col_names = ['Size of signature', '1', '5', '10']
    t.add_column(col_names[0], ['min time', 'max time', 'mean time'])
    counter = 1
    for n in [1, 5, 10]:
        mean = np.mean(times[n])
        mean_pretty = mean.seconds + round(mean.microseconds * 1e-6, 2)
        ma = max(times[n])
        ma_pretty = ma.seconds + round(ma.microseconds * 1e-6, 2)
        mi = min(times[n])
        mi_pretty = mi.seconds + round(mi.microseconds * 1e-6, 2)
        t.add_column(col_names[counter], [mi_pretty, ma_pretty, mean_pretty])
        counter += 1

    print(t)

if __name__ == '__main__':
    times_embedding, times_scoring_max, times_scoring_mean = run_experiment()
    print_table(times_embedding)
    print_table(times_scoring_max)
    print_table(times_scoring_mean)
