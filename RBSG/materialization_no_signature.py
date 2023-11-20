from rdflib.namespace import RDF, FOAF, XSD, RDFS
from rdflib import OWL, Graph, Namespace, URIRef, Literal, BNode
from rdflib.namespace import RDF, RDFS, XSD, OWL
import owlrl
import numpy as np
from math import log
import re
from prettytable import PrettyTable

class Materialization_no_signature:

    def __init__(self, g0, g):
        self.g0 = g0 #full graph
        self.g = g #shrunk graph
        self.g_ = Graph()
        self.g_ = self.g_ + g #materialized shrunk graph

    def generate_triples(self):
        """
        Only contains rdfs rules 2, 3, 5, 7, 9, 11
        """

        #rdfs2
        for s1, p1, o1 in self.g_.triples((None, RDFS.domain, None)):
            for s2, p2, o2 in self.g_.triples((None, s1, None)):
                t = (s2, RDF.type, o1) #new triple
                self.g_.add(t)

        #rdfs3
        for s1, p1, o1 in self.g_.triples((None, RDFS.range, None)):
            for s2, p2, o2 in self.g_.triples((None, s1, None)):
                t = (o2, RDF.type, o1) #new triple
                self.g_.add(t)

        #rdfs5
        for s1, p1, o1 in self.g_.triples((None, RDFS.subPropertyOf, None)):
            for s2, p2, o2 in self.g_.triples((o1, RDFS.subPropertyOf, None)):
                t = (s1, RDFS.subPropertyOf, o2) #new triple
                self.g_.add(t)

        #rdfs7
        for s1, p1, o1 in self.g_.triples((None, RDFS.subPropertyOf, None)):
            for s2, p2, o2 in self.g_.triples((None, s1, None)):
                t = (s2, o1, o2) #new triple
                self.g_.add(t)

        #rdfs9
        for s1, p1, o1 in self.g_.triples((None, RDFS.subClassOf, None)):
            for s2, p2, o2 in self.g_.triples((None, RDF.type, s1)):
                t = (s2, RDF.type, o1) #new triple
                self.g_.add(t)

        #rdfs11
        for s1, p1, o1 in self.g_.triples((None, RDFS.subClassOf, None)):
            for s2, p2, o2 in self.g_.triples((o1, RDFS.subClassOf, None)):
                t = (s1, RDFS.subClassOf, o2) #new triple
                self.g_.add(t)

    def materialize(self):
        len_old_g_ = 0
        while len_old_g_ < len(self.g_):
            #update len_old_g_ to store the current number of triples in g_
            len_old_g_ = len(self.g_)
            #generate new triples and add them to g_
            self.generate_triples()
