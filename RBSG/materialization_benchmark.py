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

from signatures import signature_dict, entity_numbers, property_numbers, class_numbers

benchmark_numbers_c = class_numbers
benchmark_numbers_p = property_numbers
benchmark_numbers_e = entity_numbers

overlap_dict = {} #stores the number of overlapping triples in the machine generated snippet and the benchamrk snippet
F1_dict = {} #stores the F1 scores

for b_n in [benchmark_numbers_e, benchmark_numbers_p, benchmark_numbers_c]:
    if b_n == benchmark_numbers_e:
        b_type = "entity"
    if b_n == benchmark_numbers_p:
        b_type = "property"
    if b_n == benchmark_numbers_c:
        b_type = "class"
    for b_number in b_n:
        signature = signature_dict[b_number]
        g = Graph()
        path_to_dataset = "Benchmark/ext_" + b_type + "/" + str(b_number) + "/" + str(b_number) + "_dataset_p.ttl"
        g.parse(path_to_dataset)
        g.parse("dbpedia_2015-10.owl")
        print(len(g))

        m = Materialization(g, g, signature)
        m.materialize()
        scores = reasoning_score(g, m.g_, signature, m.D, m.signature_triples)

        sum_m = create_summary(scores, 10) #machine generated snippet
        #sum_m = create_summary(scores, 5)

        #path_to_destination = "Benchmark/ext_" + b_type + "/" + str(b_number) + "/" + str(b_number) + "_materialization_summary.nt"
        #path_to_destination = "Benchmark/ext_" + b_type + "/" + str(b_number) + "/" + str(b_number) + "_materialization_summary_5.nt"
        #sum_m.serialize(destination=path_to_destination)

        sum_b = Graph() #benchmark snippet
        path_to_benchmark = "Benchmark/ext_" + b_type + "/" + str(b_number) + "/" + str(b_number) + "_extend.nt"
        #path_to_benchmark = "Benchmark/ext_" + b_type + "/" + str(b_number) + "/" + str(b_number) + "_extend_5.nt"
        sum_b.parse(path_to_benchmark)

        overlap_graph = sum_m & sum_b
        overlap_number = len(overlap_graph)
        overlap_dict[(b_type, b_number)] = overlap_number
        print(overlap_number)
        for t in overlap_graph:
            print(t)

        F1_dict[(b_type, b_number)] = overlap_number/10 #The F1 scores
        #F1_dict[(b_type, b_number)] = overlap_number/5

mean_overall = 0
for b_n in [benchmark_numbers_e, benchmark_numbers_p, benchmark_numbers_c]:
    temp = 0
    if b_n == benchmark_numbers_e:
        b_type = "entity"
    if b_n == benchmark_numbers_p:
        b_type = "property"
    if b_n == benchmark_numbers_c:
        b_type = "class"
    for b_number in b_n:
        temp += F1_dict[(b_type, b_number)]
        mean_overall += F1_dict[(b_type, b_number)]
    mean_F1_set = temp/len(b_n) #mean F1 score for b_n set
    print(b_type, mean_F1_set)

num_of_b = len(benchmark_numbers_e) + len(benchmark_numbers_p) + len(benchmark_numbers_c)
mean_F1_all = mean_overall/num_of_b #mean F1 score for all snippets in the benchmark
print("overall", mean_F1_all)
