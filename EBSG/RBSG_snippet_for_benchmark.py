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
from materialization import Materialization

def obtain_RBSG_scoring(signature, b_type, b_number):

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

    g = Graph()
    path_to_dataset = "Benchmark/ext_" + b_type + "/" + str(b_number) + "/" + str(b_number) + "_dataset_p.ttl"
    g.parse(path_to_dataset)
    print(len(g))

    l_set = set() #set of literals
    p_discard_set = set() #set of properties to not create an embedding for
    r_convert_set = set() #set of resources to create an embedding for

    #collect the resources to create an embedding for
    for s, p, o in g.triples((None, None, None)):
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
    path_to_KG = "Benchmark/ext_" + b_type + "/" + str(b_number) + "/" + str(b_number) + "_materialized_dataset.ttl"

    RANDOM_STATE = 22

    knowledge_graph = KG(
        location = path_to_KG
    )

    transformer = RDF2VecTransformer(
        Word2Vec(epochs=10),
        walkers=[RandomWalker(4, 10, with_reverse=False, n_jobs=1)],
    )

    embeddings, literals = transformer.fit_transform(knowledge_graph, r_convert_set)
    print(len(embeddings))

    sim_dict = {} #stores similarity score sim(x, sig) for triple element x and signature element sig

    def calculate_cosine(r, sig):
        """Computes the cosine similarity score between resource r and signature element sig"""
        r_index = r_convert_set.index(str(r))
        r_vec = embeddings[r_index]
        sig_index = r_convert_set.index(str(sig))
        sig_vec = embeddings[sig_index]
        # compute cosine similarity
        cosine = np.dot(sig_vec,r_vec)/(norm(sig_vec)*norm(r_vec))
        return cosine


    def score_element(elem):
        """Computes sim(elem, sig) for each sig in the signature"""
        if isinstance(elem, rdflib.term.Literal):
            sim_dict[elem] = [0, 0]
        elif str(elem) not in r_convert_set:
            sim_dict[elem] = [0, 0]
        else:
            sim_dict[elem] = []
            for sig in signature:
                cosine_value = calculate_cosine(elem, sig)
                sim_dict[elem].append(cosine_value)

    def score_triples():
        max_score = {} #stores the score_max scores
        mean_score = {} #stores the score_mean scores
        len_sig = len(signature)
        for s, p, o in g.triples((None, None, None)): #computes the sim scores for a triple element if not computed earlier
            if s not in sim_dict:
                score_element(s)
            if p not in sim_dict:
                score_element(p)
            if o not in sim_dict:
                score_element(o)

            #compute score_max and score_mean for triple (s, p, o)
            s_max = -1
            p_max = -1
            o_max = -1
            s_mean = 0
            p_mean = 0
            o_mean = 0
            for i in [0,1]:
                s_val = sim_dict[s][i]
                p_val = sim_dict[p][i]
                o_val = sim_dict[o][i]
                if s_val > s_max:
                    s_max = s_val
                if p_val > p_max:
                    p_max = p_val
                if o_val > o_max:
                    o_max = o_val
                s_mean += s_val
                p_mean += p_val
                o_mean += o_val
            max_score[(s, p, o)] = s_max + p_max + o_max
            mean_score[(s, p, o)] = s_mean/len_sig + p_mean/len_sig + o_mean/len_sig
        return max_score, mean_score

    return score_triples()

if __name__ == '__main__':
    obtain_RBSG_scoring()
