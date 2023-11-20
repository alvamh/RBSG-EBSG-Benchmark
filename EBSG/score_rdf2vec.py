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

def score_triples_max(r_convert_set, embeddings, g, signature, n):

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


    def score_element(elem, n):
        """Computes sim(elem, sig) for each sig in the signature"""
        if isinstance(elem, rdflib.term.Literal):
            sim_dict[elem] = [0] * n
        elif str(elem) not in r_convert_set:
            sim_dict[elem] = [0] * n
        else:
            sim_dict[elem] = []
            for sig in signature:
                cosine_value = calculate_cosine(elem, sig)
                sim_dict[elem].append(cosine_value)

    max_score = {} #stores the score_max scores
    for s, p, o in g.triples((None, None, None)): #computes the sim scores for a triple element if not computed earlier
        if s not in sim_dict:
            score_element(s, n)
        if p not in sim_dict:
            score_element(p, n)
        if o not in sim_dict:
            score_element(o, n)

        #compute score_max for triple (s, p, o)
        s_max = -1
        p_max = -1
        o_max = -1
        for i in range(n):
            s_val = sim_dict[s][i]
            p_val = sim_dict[p][i]
            o_val = sim_dict[o][i]
            if s_val > s_max:
                s_max = s_val
            if p_val > p_max:
                p_max = p_val
            if o_val > o_max:
                o_max = o_val
        max_score[(s, p, o)] = s_max + p_max + o_max

    return max_score

def score_triples_mean(r_convert_set, embeddings, g, signature, n):

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

    def score_element(elem, n):
        """Computes sim(elem, sig) for each sig in the signature"""
        if isinstance(elem, rdflib.term.Literal):
            sim_dict[elem] = [0] * n
        elif str(elem) not in r_convert_set:
            sim_dict[elem] = [0] * n
        else:
            sim_dict[elem] = []
            for sig in signature:
                cosine_value = calculate_cosine(elem, sig)
                sim_dict[elem].append(cosine_value)

    mean_score = {} #stores the score_mean scores
    len_sig = len(signature)
    for s, p, o in g.triples((None, None, None)): #computes the sim scores for a triple element if not computed earlier
        if s not in sim_dict:
            score_element(s, n)
        if p not in sim_dict:
            score_element(p, n)
        if o not in sim_dict:
            score_element(o, n)

        #compute score_mean for triple (s, p, o)
        s_mean = 0
        p_mean = 0
        o_mean = 0
        for i in range(n):
            s_val = sim_dict[s][i]
            p_val = sim_dict[p][i]
            o_val = sim_dict[o][i]
            s_mean += s_val
            p_mean += p_val
            o_mean += o_val
        mean_score[(s, p, o)] = s_mean/len_sig + p_mean/len_sig + o_mean/len_sig

    return mean_score
