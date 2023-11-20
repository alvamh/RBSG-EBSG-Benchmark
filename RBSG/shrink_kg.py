from rdflib.namespace import RDF, FOAF, XSD, RDFS, OWL
from rdflib import OWL, Graph, Namespace, URIRef, Literal, BNode
import owlrl
import numpy as np
from math import log
import re

class Shrink_kg:

    def __init__(self, S):
        self.S = S

    def add_to_S(self, triple):
        special_predicates = {RDF.type, RDF.Property, RDFS.subPropertyOf,
                              RDFS.Class, RDFS.subClassOf, RDFS.Resource,
                              RDFS.domain, RDFS.range, RDFS.label}
        special_objects = {OWL.Class, OWL.DatatypeProperty, OWL.Thing}

        s, p, o = triple[0], triple[1], triple[2]

        if s not in self.S:
            self.S.append(s)
        if p not in special_predicates:
            if p not in self.S:
                self.S.append(p)
        if o not in special_objects:
            if o not in self.S:
                self.S.append(o)

    def solve(self, g):
        g_ = Graph() #shrunken graph
        S_old = list() #previous version of the signature, initially an empty list
        while S_old < self.S:
            S_old = self.S.copy() #update S_old to be the current signature
            for e in self.S:
                subjects = g.triples((e, None, None))
                predicates = g.triples((None, e, None))
                objects = g.triples((None, None, e))
                for t in subjects:
                    self.add_to_S(t)
                    g_.add(t)
                for t in predicates:
                    self.add_to_S(t)
                    g_.add(t)
                for t in objects:
                    self.add_to_S(t)
                    g_.add(t)

        return g_
