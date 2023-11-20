from rdflib.namespace import RDF, FOAF, XSD, RDFS, OWL
from rdflib import OWL, Graph, Namespace, URIRef, Literal, BNode
import owlrl
import numpy as np
from math import log
import re
from prettytable import PrettyTable
from datetime import datetime, time, timedelta

class Materialization:

    def __init__(self, g0, g, S):
        """
        Makes a dictionary to store which  original triples are used to
        generate which new triples.
        """
        self.g0 = g0 #full graph
        self.g = g #shrunk graph if shrinking algorithm was used, otherwise g=g0
        self.g_ = Graph()
        self.g_ = self.g_ + self.g #materialized graph
        self.S = S #signature
        self.D = {} #dictionary to store premise triples and entailed triples
        self.signature_triples = [] #triples containing a signature element
        self.timeToSubstract = timedelta() #time spent on adding triples to D
        startTime_dict = datetime.now()
        for triple in self.g:
            self.D[triple] = {}
            for e in self.S:
                self.D[triple][e] = Graph()
                if e in triple:
                    self.D[triple][e] = self.D[triple][e].add(triple)
                    self.signature_triples.append(triple)
        endTime_dict = datetime.now()
        self.timeToSubstract = self.timeToSubstract + (endTime_dict - startTime_dict)

    def generate_triples(self):
        """
        Only contains rdfs rules 2, 3, 5, 7, 9, 11
        """

        #rdfs2
        for s1, p1, o1 in self.g_.triples((None, RDFS.domain, None)):
            for s2, p2, o2 in self.g_.triples((None, s1, None)):
                t = (s2, RDF.type, o1) #new triple
                #The new generated triple is only of interest if it contains at
                #least one of the resources in the signature, and it is
                #not already in the original KG
                if ((s2 in self.S) or (o1 in self.S)) and (t not in self.g):
                    self.g_.add(t)
                    startTime_dict = datetime.now()
                    if s2 in self.S:
                        if (s1, p1, o1) in self.D:
                            self.D[(s1, p1, o1)][s2] = self.D[(s1, p1, o1)][s2].add(t)
                        if (s2, p2, o2) in self.D:
                            self.D[(s2, p2, o2)][s2] = self.D[(s2, p2, o2)][s2].add(t)
                    if o1 in self.S:
                        if (s1, p1, o1) in self.D:
                            self.D[(s1, p1, o1)][o1] = self.D[(s1, p1, o1)][o1].add(t)
                        if (s2, p2, o2) in self.D:
                            self.D[(s2, p2, o2)][o1] = self.D[(s2, p2, o2)][o1].add(t)
                    endTime_dict = datetime.now()
                    self.timeToSubstract = self.timeToSubstract + (endTime_dict - startTime_dict)

        #rdfs3
        for s1, p1, o1 in self.g_.triples((None, RDFS.range, None)):
            for s2, p2, o2 in self.g_.triples((None, s1, None)):
                t = (o2, RDF.type, o1) #new triple
                if ((o2 in self.S) or (o1 in self.S)) and (t not in self.g):
                    self.g_.add(t)
                    startTime_dict = datetime.now()
                    if o2 in self.S:
                        if (s1, p1, o1) in self.D:
                            self.D[(s1, p1, o1)][o2] = self.D[(s1, p1, o1)][o2].add(t)
                        if (s2, p2, o2) in self.D:
                            self.D[(s2, p2, o2)][o2] = self.D[(s2, p2, o2)][o2].add(t)
                    if o1 in self.S:
                        if (s1, p1, o1) in self.D:
                            self.D[(s1, p1, o1)][o1] = self.D[(s1, p1, o1)][o1].add(t)
                        if (s2, p2, o2) in self.D:
                            self.D[(s2, p2, o2)][o1] = self.D[(s2, p2, o2)][o1].add(t)
                    endTime_dict = datetime.now()
                    self.timeToSubstract = self.timeToSubstract + (endTime_dict - startTime_dict)

        #rdfs5
        for s1, p1, o1 in self.g_.triples((None, RDFS.subPropertyOf, None)):
            for s2, p2, o2 in self.g_.triples((o1, RDFS.subPropertyOf, None)):
                t = (s1, RDFS.subPropertyOf, o2) #new triple
                if ((s1 in self.S) or (o2 in self.S)) and (t not in self.g):
                    self.g_.add(t)
                    startTime_dict = datetime.now()
                    if s1 in self.S:
                        if (s1, p1, o1) in self.D:
                            self.D[(s1, p1, o1)][s1] = self.D[(s1, p1, o1)][s1].add(t)
                        if (s2, p2, o2) in self.D:
                            self.D[(s2, p2, o2)][s1] = self.D[(s2, p2, o2)][s1].add(t)
                    if o2 in self.S:
                        if (s1, p1, o1) in self.D:
                            self.D[(s1, p1, o1)][o2] = self.D[(s1, p1, o1)][o2].add(t)
                        if (s2, p2, o2) in self.D:
                            self.D[(s2, p2, o2)][o2] = self.D[(s2, p2, o2)][o2].add(t)
                    endTime_dict = datetime.now()
                    self.timeToSubstract = self.timeToSubstract + (endTime_dict - startTime_dict)


        #rdfs7
        for s1, p1, o1 in self.g_.triples((None, RDFS.subPropertyOf, None)):
            for s2, p2, o2 in self.g_.triples((None, s1, None)):
                t = (s2, o1, o2) #new triple
                if ((s2 in self.S) or (o1 in self.S) or (o2 in self.S)) and (t not in self.g):
                    self.g_.add(t)
                    startTime_dict = datetime.now()
                    if s2 in self.S:
                        if (s1, p1, o1) in self.D:
                            self.D[(s1, p1, o1)][s2] = self.D[(s1, p1, o1)][s2].add(t)
                        if (s2, p2, o2) in self.D:
                            self.D[(s2, p2, o2)][s2] = self.D[(s2, p2, o2)][s2].add(t)
                    if o1 in self.S:
                        if (s1, p1, o1) in self.D:
                            self.D[(s1, p1, o1)][o1] = self.D[(s1, p1, o1)][o1].add(t)
                        if (s2, p2, o2) in self.D:
                            self.D[(s2, p2, o2)][o1] = self.D[(s2, p2, o2)][o1].add(t)
                    if o2 in self.S:
                        if (s1, p1, o1) in self.D:
                            self.D[(s1, p1, o1)][o2] = self.D[(s1, p1, o1)][o2].add(t)
                        if (s2, p2, o2) in self.D:
                            self.D[(s2, p2, o2)][o2] = self.D[(s2, p2, o2)][o2].add(t)
                    endTime_dict = datetime.now()
                    self.timeToSubstract = self.timeToSubstract + (endTime_dict - startTime_dict)


        #rdfs9
        for s1, p1, o1 in self.g_.triples((None, RDFS.subClassOf, None)):
            for s2, p2, o2 in self.g_.triples((None, RDF.type, s1)):
                t = (s2, RDF.type, o1) #new triple
                if ((s2 in self.S) or (o1 in self.S)) and (t not in self.g):
                    self.g_.add(t)
                    startTime_dict = datetime.now()
                    if s2 in self.S:
                        if (s1, p1, o1) in self.D:
                            self.D[(s1, p1, o1)][s2] = self.D[(s1, p1, o1)][s2].add(t)
                        if (s2, p2, o2) in self.D:
                            self.D[(s2, p2, o2)][s2] = self.D[(s2, p2, o2)][s2].add(t)
                    if o1 in self.S:
                        if (s1, p1, o1) in self.D:
                            self.D[(s1, p1, o1)][o1] = self.D[(s1, p1, o1)][o1].add(t)
                        if (s2, p2, o2) in self.D:
                            self.D[(s2, p2, o2)][o1] = self.D[(s2, p2, o2)][o1].add(t)
                    endTime_dict = datetime.now()
                    self.timeToSubstract = self.timeToSubstract + (endTime_dict - startTime_dict)


        #rdfs11
        for s1, p1, o1 in self.g_.triples((None, RDFS.subClassOf, None)):
            for s2, p2, o2 in self.g_.triples((o1, RDFS.subClassOf, None)):
                t = (s1, RDFS.subClassOf, o2) #new triple
                if ((s1 in self.S) or (o2 in self.S)) and (t not in self.g):
                    self.g_.add(t)
                    startTime_dict = datetime.now()
                    if s1 in self.S:
                        if (s1, p1, o1) in self.D:
                            self.D[(s1, p1, o1)][s1] = self.D[(s1, p1, o1)][s1].add(t)
                        if (s2, p2, o2) in self.D:
                            self.D[(s2, p2, o2)][s1] = self.D[(s2, p2, o2)][s1].add(t)
                    if o2 in self.S:
                        if (s1, p1, o1) in self.D:
                            self.D[(s1, p1, o1)][o2] = self.D[(s1, p1, o1)][o2].add(t)
                        if (s2, p2, o2) in self.D:
                            self.D[(s2, p2, o2)][o2] = self.D[(s2, p2, o2)][o2].add(t)
                    endTime_dict = datetime.now()
                    self.timeToSubstract = self.timeToSubstract + (endTime_dict - startTime_dict)


    def materialize(self):
        len_old_g_ = 0
        while len_old_g_ < len(self.g_):
            #update len_old_g_ to store the current number of triples in g_
            len_old_g_ = len(self.g_)
            #generate new triples and add them to g_
            self.generate_triples()
