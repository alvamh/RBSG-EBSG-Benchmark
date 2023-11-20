import sys
from rdflib.namespace import RDF, FOAF, XSD, RDFS, OWL
from rdflib import OWL, Graph, Namespace, URIRef, Literal, BNode, term
import owlrl
import numpy as np
from math import log
import re
from prettytable import PrettyTable
import random
from datetime import datetime, time, timedelta
import statistics as stat

from shrink_kg import Shrink_kg
from materialization import Materialization
from materialization_score import reasoning_score
from create_summary import create_summary
from make_signature import make_signature
from materialization_no_signature import Materialization_no_signature

g = Graph()
g_mapping  = Graph()
ent_set = set() #set with instance level entities to make signatures
res_set = set() #set with resources to make signatures
g.parse("Dataset_experiment_shrinking\mappingbased_properties_en_a_small.ttl")
g_mapping.parse("Dataset_experiment_shrinking\mappingbased_properties_en_a_small.ttl")
print(len(g))
for s, p, o in g_mapping.triples((None, None, None)):
    ent_set.add(s)
g.parse("Dataset_experiment_shrinking\instance_types_en_a_small.ttl")
print(len(g))
for s, p, o in g.triples((None, None, None)):
    if p == RDF.type:
        res_set.add(s)
        res_set.add(o)
    else:
        res_set.add(s)
        res_set.add(p)
        if not isinstance(o, term.Literal):
            res_set.add(o)
g.parse("Dataset_experiment_shrinking\dbpedia_small.ttl") #dataset with relevant ontology triples
print(len(g))

def run_experiment(signature_type):
    times_mat = {} #running time for the materialization algorithm using the original graph
    size_mat_graph = {} #size of the materialized original graph
    times_shrink = {} #running time for the shrinking algorithm
    size_shrunk_graph = {} #size of the shrunken graph
    times_mat_shrunk = {} #running time for the materialization algorithm using the shrunken graph
    size_mat_shrunk_graph = {} #size of the materialized shrunken graph

    for n in [1, 5, 10]: #signature-sizes
        times_mat[n] = []
        size_mat_graph[n] = []
        times_shrink[n] = []
        size_shrunk_graph[n] = []
        times_mat_shrunk[n] = []
        size_mat_shrunk_graph[n] = []

        for i in range(2):
            sign_init = make_signature(n, g_mapping, g, list(ent_set), list(res_set), signature_type)
            print(n, i)
            for sig in sign_init:
                print(sig)
            sign_shrink = sign_init.copy()

            #materialization with original graph
            startTime = datetime.now()
            m = Materialization(g, g, sign_init)
            m.materialize()
            timeToSubstract = m.timeToSubstract
            endTime = datetime.now()
            times_mat[n].append((endTime - startTime) - timeToSubstract)
            size_mat_graph[n].append(len(m.g_)-len(g))

            #shrink the original graph
            startTime = datetime.now()
            sh = Shrink_kg(sign_shrink)
            g_shrunk = sh.solve(g)
            endTime = datetime.now()
            times_shrink[n].append(endTime - startTime)
            size_shrunk_graph[n].append(len(g)-len(g_shrunk))

            #materialization with shrunk graph
            startTime = datetime.now()
            m_s = Materialization(g, g_shrunk, sign_init)
            m_s.materialize()
            timeToSubstract = m_s.timeToSubstract
            endTime = datetime.now()
            times_mat_shrunk[n].append((endTime - startTime) - timeToSubstract)
            size_mat_shrunk_graph[n].append(len(m_s.g_)-len(g_shrunk))

    return times_mat, size_mat_graph, times_shrink, size_shrunk_graph, times_mat_shrunk, size_mat_shrunk_graph

def print_table(times, size_graph, signature_type):
    t = PrettyTable()
    col_names = ['Size of signature', '1', '5', '10']
    t.add_column(col_names[0], ['min time', 'max time', 'mean time', 'min size g´', 'max size g´', 'mean size g´'])
    counter = 1
    for n in [1, 5, 10]:
        mean = np.mean(times[n])
        mean_pretty = mean.seconds + round(mean.microseconds * 1e-6, 2)
        ma = max(times[n])
        ma_pretty = ma.seconds + round(ma.microseconds * 1e-6, 2)
        mi = min(times[n])
        mi_pretty = mi.seconds + round(mi.microseconds * 1e-6, 2)
        mean_size = np.mean(size_graph[n])
        max_size = max(size_graph[n])
        min_size = min(size_graph[n])
        t.add_column(col_names[counter], [mi_pretty, ma_pretty, mean_pretty, min_size, max_size, mean_size])
        counter += 1

    print(t)

#run experiment with random signature and seed signature

times_mat_random, size_mat_graph_random, times_shrink_random, size_shrunk_graph_random, times_mat_shrunk_random, size_mat_shrunk_graph_random = run_experiment("random")
times_mat_seed, size_mat_graph_seed, times_shrink_seed, size_shrunk_graph_seed, times_mat_shrunk_seed, size_mat_shrunk_graph_seed = run_experiment("seed")
print("RANDOM")
print_table(times_mat_random, size_mat_graph_random, "random")
print_table(times_shrink_random, size_shrunk_graph_random, "random")
print_table(times_mat_shrunk_random, size_mat_shrunk_graph_random, "random")
print("SEED")
print_table(times_mat_seed, size_mat_graph_seed, "seed")
print_table(times_shrink_seed, size_shrunk_graph_seed, "seed")
print_table(times_mat_shrunk_seed, size_mat_shrunk_graph_seed, "seed")
