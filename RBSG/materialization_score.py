from rdflib.namespace import RDF, FOAF, XSD, RDFS, OWL
from rdflib import OWL, Graph, Namespace, URIRef, Literal, BNode
import owlrl
import numpy as np
from math import log
import re
from prettytable import PrettyTable

def reasoning_score(g, g_, S, D, signature_triples):
    """
    g: original graph or shrunk graph
    g_: materialized graph
    S: signature
    D: contains info about which triples can
       be used to generate new triples
    """
    scores = {}
    new_triples = Graph() #graph containing the enteiled triples
    new_triples = g_ - g
    for t in signature_triples:
        new_triples.add(t) #original triples containing a signature element
    num_triples_resource = {} #number of entailed triples containing resource r
    for r in S:
        num_triples_resource[r] = 0
        for triple in new_triples:
            if r in triple:
                num_triples_resource[r] += 1

    for triple, resource_values in D.items(): #triple is a triple in the original KG, resource_values is a dictionary
        scores[triple] = 0
        for r, value in resource_values.items(): #r is an element in the signature, value is the number of entailments
                                                 #containing r that triple can generate 
            if len(value) > 0:
                scores[triple] += len(value)/num_triples_resource[r]/len(S)

    return scores
