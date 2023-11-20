from pyrdf2vec import RDF2VecTransformer
from pyrdf2vec.embedders import Word2Vec
from pyrdf2vec.graphs import KG
from pyrdf2vec.walkers import RandomWalker
import random
import rdflib
from rdflib import Graph, URIRef
import numpy as np
from numpy.linalg import norm
from create_summary import create_summary

def rdf2vec_func(g_data):

    general_predicates = [
    "http://purl.org/dc/terms/subject",
    "http://xmlns.com/foaf/0.1/homepage",
    "http://xmlns.com/foaf/0.1/depiction",
    "http://www.w3.org/2000/01/rdf-schema#label",
    "http://www.w3.org/1999/02/22-rdf-syntax-ns#type",
    "http://www.w3.org/2000/01/rdf-schema#seeAlso",
    "http://xmlns.com/foaf/0.1/name",
    "http://www.w3.org/2002/07/owl#differentFrom",
    "http://www.w3.org/2003/01/geo/wgs84_pos#lat",
    "http://www.w3.org/2003/01/geo/wgs84_pos#long",
    "http://www.georss.org/georss/point",
    "http://www.w3.org/2004/02/skos/core#subject",
    "http://xmlns.com/foaf/0.1/nick",
    "http://xmlns.com/foaf/0.1/givenName",
    "http://xmlns.com/foaf/0.1/page",
    "http://purl.org/dc/elements/1.1/description",
    "http://xmlns.com/foaf/0.1/surname",
    "http://purl.org/dc/elements/1.1/type",
    "http://xmlns.com/foaf/0.1/thumbnail",
    "http://xmlns.com/foaf/0.1/logo",
    "http://xmlns.com/foaf/0.1/familyName",
    "http://purl.org/dc/elements/1.1/rights",
    "http://dbpedia.org/ontology/category",
    "http://dbpedia.org/ontology/type",
    "http://dbpedia.org/ontology/otherName"
    ]

    l_set = set() #set of literals
    p_discard_set = set() #set of properties to not create an embedding for
    r_convert_set = set() #set of resources to create an embedding for

    #collect the resources to create an embedding for
    for s, p, o in g_data.triples((None, None, None)):
        if o != URIRef("http://www.w3.org/1999/02/22-rdf-syntax-ns#Property"):
            r_convert_set.add(str(s))
            if str(p) in general_predicates:
                p_discard_set.add(str(p))
            else:
                r_convert_set.add(str(p))
        if isinstance(o, rdflib.term.Literal):
            l_set.add(o)
        else: r_convert_set.add(str(o))

    r_convert_set.remove("http://www.w3.org/1999/02/22-rdf-syntax-ns#Property")
    r_convert_set = list(r_convert_set)


    #obtain the embeddings
    RANDOM_STATE = 22

    knowledge_graph = KG(
        location = "data_ont_reduced.ttl"
    )

    transformer = RDF2VecTransformer(
        Word2Vec(epochs=10),
        walkers=[RandomWalker(4, 10, with_reverse=False, n_jobs=1)],
    )

    embeddings, literals = transformer.fit_transform(knowledge_graph, r_convert_set)
    print("len embed ", len(embeddings))

    return embeddings, r_convert_set

if __name__ == '__main__':
    g_data = Graph()
    g_data.parse("dataset_en_reduced_reduced.ttl")
    func(g_data)
