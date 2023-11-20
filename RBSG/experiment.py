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

from materialization import Materialization
from materialization_score import reasoning_score
from create_summary import create_summary
from make_signature import make_signature
from materialization_no_signature import Materialization_no_signature

g = Graph()
g_mapping  = Graph()
ent_set = set() #set with instance level entities to make signatures
res_set = set() #set with resources to make signatures
g.parse("Dataset_experiment_main\mappingbased_objects_en_reduced_reduced_p.ttl")
g_mapping.parse("Dataset_experiment_main\mappingbased_objects_en_reduced_reduced_p.ttl")
print(len(g))
for s, p, o in g_mapping.triples((None, None, None)):
    ent_set.add(s)
g.parse("Dataset_experiment_main\instance_types_en_reduced_reduced_p.ttl")
print(len(g))
for s, p, o in g.triples((None, None, None)):
    if p == RDF.type:
        res_set.add(s)
        res_set.add(o)
    else:
        res_set.add(s)
        res_set.add(p)
        res_set.add(o)
res_set.remove(URIRef("http://www.w3.org/1999/02/22-rdf-syntax-ns#Property"))
g.parse("Dataset_experiment_main\ontology_2015-10_reduced.ttl") #dataset with relevant ontology triples
print(len(g))

def run_experiment(signature_type):
    times = {} #running time for the materialization algorithm
    times_score = {} #running time for scoring, ranking and creating a snippet
    size_graph = {} #size of the materialized graph
    times_add_to_dict = {} #time spent on adding entailed triples to a dictionary

    if (signature_type == "random") or (signature_type == "seed"):
        for n in [1, 5, 10]: #signature-sizes
            times[n] = []
            times_score[n] = []
            size_graph[n] = []
            times_add_to_dict[n] = []

            for i in range(100):
                sign_init = make_signature(n, g_mapping, g, list(ent_set), list(res_set), signature_type)
                print(n, i)
                for sig in sign_init:
                    print(sig)
                startTime = datetime.now()
                m = Materialization(g, g, sign_init)
                m.materialize()
                timeToSubstract = m.timeToSubstract
                endTime = datetime.now()
                times[n].append((endTime - startTime) - timeToSubstract)
                size_graph[n].append(len(m.g_))
                times_add_to_dict[n].append(timeToSubstract)
                startTime = datetime.now()
                scores = reasoning_score(g, m.g_, sign_init, m.D, m.signature_triples)
                sum_m = create_summary(scores, 5)
                endTime = datetime.now()
                times_score[n].append(endTime - startTime)

    if signature_type == "no_signature":
        times[0] = []
        size_graph[0] = []
        for i in range(100):
            print(i)
            startTime = datetime.now()
            m = Materialization_no_signature(g, g)
            m.materialize()
            endTime = datetime.now()
            times[0].append(endTime - startTime)
            size_graph[0].append(len(m.g_))

    return times, times_score, size_graph, times_add_to_dict

def print_table(times, signature_type, size_graph = None):
    t = PrettyTable()
    if (signature_type == "random") or (signature_type == "seed"):
        col_names = ['Size of signature', '1', '5', '10']
        if size_graph != None:
            t.add_column(col_names[0], ['min time', 'max time', 'mean time', 'min size g´', 'max size g´', 'mean size g´'])
        else:
            t.add_column(col_names[0], ['min time', 'max time', 'mean time'])
        counter = 1
        for n in [1, 5, 10]:
            mean = np.mean(times[n])
            mean_pretty = mean.seconds + round(mean.microseconds * 1e-6, 2)
            ma = max(times[n])
            ma_pretty = ma.seconds + round(ma.microseconds * 1e-6, 2)
            mi = min(times[n])
            mi_pretty = mi.seconds + round(mi.microseconds * 1e-6, 2)
            if  size_graph != None:
                mean_size = np.mean(size_graph[n])
                max_size = max(size_graph[n])
                min_size = min(size_graph[n])
                t.add_column(col_names[counter], [mi_pretty, ma_pretty, mean_pretty, min_size, max_size, mean_size])
            else:
                t.add_column(col_names[counter], [mi_pretty, ma_pretty, mean_pretty])
            counter += 1

    if signature_type == "no_signature":
        col_names = ['Size of signature', 'No signature']
        t.add_column(col_names[0], ['min time', 'max time', 'mean time', 'min size g´', 'max size g´', 'mean size g´'])
        mean = np.mean(times[0])
        mean_pretty = mean.seconds + round(mean.microseconds * 1e-6, 2)
        ma = max(times[0])
        ma_pretty = ma.seconds + round(ma.microseconds * 1e-6, 2)
        mi = min(times[0])
        mi_pretty = mi.seconds + round(mi.microseconds * 1e-6, 2)
        mean_size = np.mean(size_graph[0])
        max_size = max(size_graph[0])
        min_size = min(size_graph[0])
        t.add_column(col_names[1], [mi_pretty, ma_pretty, mean_pretty, min_size, max_size, mean_size])

    print(t)

#run experiment with random signature, seed signature and no signature

times_random, times_score_random, size_graph_random, times_add_to_dict_random = run_experiment("random")
times_seed, times_score_seed, size_graph_seed, times_add_to_dict_seed = run_experiment("seed")
times_none, times_score_none, size_graph_none, times_add_to_dict_none = run_experiment("no_signature") #times_score_none and times_add_to_dict_none is empty dictionaries
print("RANDOM")
print_table(times_random, "random", size_graph_random)
print_table(times_score_random, "random")
print_table(times_add_to_dict_random, "random")
print("SEED")
print_table(times_seed, "seed", size_graph_seed)
print_table(times_score_seed, "seed")
print_table(times_add_to_dict_seed, "seed")
print("NO SIGNATURE")
print_table(times_none, "no_signature", size_graph_none)
