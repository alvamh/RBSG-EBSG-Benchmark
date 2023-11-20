from rdflib import Graph
import re
from prettytable import PrettyTable

def create_summary(scores, k):
    sorted_scores = [(ke, va) for ke, va in sorted(scores.items(), key=lambda x: x[1], reverse=True)]
    k_triples = sorted_scores[0:k] #top k triples
    res = Graph() #the generated snippet as a graph
    t = PrettyTable(['Triple', 'Total Score'])
    for tuple in k_triples:
        key = tuple[0]
        value = tuple[1]
        res.add(key)
        s = re.split('/ | #', key[0])[-1]
        p = re.split('/ | #', key[1])[-1]
        o = re.split('/ | #', key[2])[-1]
        t.add_row([(s, p, o), round(value, 2)])
    print(t)
    return res
