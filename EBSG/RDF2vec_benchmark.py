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

from create_summary import create_summary
from RBSG_snippet_for_benchmark import obtain_RBSG_scoring

from signatures import signature_dict, entity_numbers, property_numbers, class_numbers

def RDF2Vec_benchmark_function():

    benchmark_numbers_c = class_numbers
    benchmark_numbers_p = property_numbers
    benchmark_numbers_e = entity_numbers

    F1_5_max_dict = {} #stores F1 scores for top-5 snippets where score_max was used
    F1_10_max_dict = {} #stores F1 scores for top-10 snippets where score_max was used
    F1_5_mean_dict = {} #stores F1 scores for top-5 snippets where score_mean was used
    F1_10_mean_dict = {} #stores F1 scores for top-10 snippets where score_mean was used

    for b_n in [benchmark_numbers_e, benchmark_numbers_p, benchmark_numbers_c]:
        if b_n == benchmark_numbers_e:
            b_type = "entity"
        if b_n == benchmark_numbers_p:
            b_type = "property"
        if b_n == benchmark_numbers_c:
            b_type = "class"
        for b_number in b_n:
            signature = signature_dict[b_number]
            max_score, mean_score = obtain_RBSG_scoring(signature, b_type, b_number) #obtain the triple scores from using RBSG

            #create top-5 and top-10 snippets using the score_max scores and score_mean scores
            top_5_max = create_summary(max_score, 5)
            top_10_max = create_summary(max_score, 10)
            top_5_mean = create_summary(mean_score, 5)
            top_10_mean = create_summary(mean_score, 10)

            #obtain the benchmark snippets
            sum_b_5 = Graph()
            sum_b_10 = Graph()
            path_to_benchmark_5 = "Benchmark/ext_" + b_type + "/" + str(b_number) + "/" + str(b_number) + "_extend_5.nt"
            path_to_benchmark_10 = "Benchmark/ext_" + b_type + "/" + str(b_number) + "/" + str(b_number) + "_extend.nt"
            sum_b_5.parse(path_to_benchmark_5)
            sum_b_10.parse(path_to_benchmark_10)

            #compute the overlap between a RBSG snippet and a benchmark snippet
            overlap_graph_5_max = top_5_max & sum_b_5
            overlap_number_5_max = len(overlap_graph_5_max)
            overlap_graph_10_max = top_10_max & sum_b_10
            overlap_number_10_max = len(overlap_graph_10_max)
            overlap_graph_5_mean = top_5_mean & sum_b_5
            overlap_number_5_mean = len(overlap_graph_5_mean)
            overlap_graph_10_mean = top_10_mean & sum_b_10
            overlap_number_10_mean = len(overlap_graph_10_mean)

            #compute F1 scores
            F1_5_max_dict[(b_type, b_number)] = overlap_number_5_max/5
            F1_10_max_dict[(b_type, b_number)] = overlap_number_10_max/10
            F1_5_mean_dict[(b_type, b_number)] = overlap_number_5_mean/5
            F1_10_mean_dict[(b_type, b_number)] = overlap_number_10_mean/10

    #compute mean F1 score for each type of signature and for all signatures
    mean_overall_5_max = 0
    mean_overall_10_max = 0
    mean_overall_5_mean = 0
    mean_overall_10_mean = 0
    for b_n in [benchmark_numbers_e, benchmark_numbers_p, benchmark_numbers_c]:
        temp_5_max = 0
        temp_10_max = 0
        temp_5_mean = 0
        temp_10_mean = 0
        if b_n == benchmark_numbers_e:
            b_type = "entity"
        if b_n == benchmark_numbers_p:
            b_type = "property"
        if b_n == benchmark_numbers_c:
            b_type = "class"
        for b_number in b_n:
            temp_5_max += F1_5_max_dict[(b_type, b_number)]
            mean_overall_5_max += F1_5_max_dict[(b_type, b_number)]
            temp_10_max += F1_10_max_dict[(b_type, b_number)]
            mean_overall_10_max += F1_10_max_dict[(b_type, b_number)]
            temp_5_mean += F1_5_mean_dict[(b_type, b_number)]
            mean_overall_5_mean += F1_5_mean_dict[(b_type, b_number)]
            temp_10_mean += F1_10_mean_dict[(b_type, b_number)]
            mean_overall_10_mean += F1_10_mean_dict[(b_type, b_number)]
        print(b_type, temp_5_max/len(b_n))
        print(b_type, temp_10_max/len(b_n))
        print(b_type, temp_5_mean/len(b_n))
        print(b_type, temp_10_mean/len(b_n))

    num_of_b = len(benchmark_numbers_e) + len(benchmark_numbers_p) + len(benchmark_numbers_c)
    print("overall 5 max", mean_overall_5_max/num_of_b)
    print("overall 10 max", mean_overall_10_max/num_of_b)
    print("overall 5 mean", mean_overall_5_mean/num_of_b)
    print("overall 10 mean", mean_overall_10_mean/num_of_b)

if __name__ == '__main__':
    RDF2Vec_benchmark_function()
