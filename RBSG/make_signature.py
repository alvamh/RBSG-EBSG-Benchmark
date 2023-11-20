import random
from rdflib import URIRef
from rdflib.namespace import RDF, FOAF, XSD, RDFS

def make_signature(n, g_mapping, g, ent_set, res_set, type):

    if type == "random":
        signature = []
        signature.append(random.choice(ent_set)) #at least one entity in the signature
        if n > 1:
            rest = random.choices(res_set, k=(n-1)) #the rest of the elements in the signature
                                                    #can be any resource
            for r in rest:
                signature.append(r)

    if type == "seed":
        sig = set()

        def add_to_signature(tup):
            for s, p, o in g.triples(tup):
                if (len(sig) < n) and (p != RDF.type):
                    sig.add(p)
                if len(sig) < n:
                    sig.add(o)
                if len(sig) == n:
                    break

        def get_triple(e):
            for s, p, o in g_mapping.triples((e, None, None)):
                break
            return p, o

        start_entity = random.choice(ent_set) #at least one entity in the signature
        sig.add(start_entity)
        if (n == 5) or (n == 10):
            start_property, start_value = get_triple(start_entity)
            sig.add(start_property)
            sig.add(start_value)
            for s, p, o in g.triples((start_entity, RDF.type, None)):
                sig.add(o)
                break
            for s, p, o in g.triples((start_value, RDF.type, None)):
                sig.add(o)
                break
            while len(sig) < n:
                add_to_signature((start_entity, None, None))
                if len(sig) < n:
                    add_to_signature((start_value, None, None))
                if len(sig) < n:
                    start_entity = random.choice(ent_set)
                    sig.add(start_entity)
                    start_property, start_value = get_triple(start_entity)

        signature = list(sig)

    return signature
