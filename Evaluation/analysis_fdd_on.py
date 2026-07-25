# -*- coding: utf-8 -*-
"""
Created on Fri Apr 3 17:49:05 2026

# Name: analysis_fdd_on.py

@author: Yimin Chen

# Project Name: FDD-ON ontology development

 
    


"""

from rdflib import Graph, Namespace
from rdflib.namespace import RDF, RDFS

# from rdflib import Graph, Namespace, RDF, RDFS, URIRef

# 1. Initialize graph and parse the RDF file
g = Graph()
g.parse("FDD_ON_VAV_HVAC.rdf", format = "xml")

# 2. Use SPARQL query to query data
# Using `rdfs:subClassOf+` finds all subclasses transitively (direct and indirect)
# Replace `rdfs:subClassOf+` with `rdfs:subClassOf` if you ONLY want direct children

query = """
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    
    SELECT DISTINCT ?subclass
    WHERE {
        ?subclass rdfs:subClassOf+ ?parent .
        FILTER (strends(str(?parent), "AHU-Fault") || strends(str(?parent), "#AHU-Fault"))
    }
"""

results = g.query(query)
subclasses = [str(row.subclass) for row in results]

print(f"Total subclasses under 'AHU-Fault': {len(subclasses)}\n")
for sc in subclasses:
    print(f" - {sc}")
    
    
    
'''    
# %% Another method

ahu_fault_uri = None
for s in g.subjects():
    if str(s).endswith("AHU-Fault") or str(s).endswith("#AHU-Fault"):
        ahu_fault_uri = s
        break

subclasses = []

if ahu_fault_uri:
    # transitive_subjects finds all direct and indirect subclasses of ahu_fault_uri
    all_subclasses = set(g.transitive_subjects(RDFS.subClassOf, ahu_fault_uri))
    
    # Exclude the class itself from the results
    subclasses = [str(sc) for sc in all_subclasses if sc != ahu_fault_uri]

# 3. Print results
print(f"Total subclasses under 'AHU-Fault': {len(subclasses)}\n")
for sc in subclasses:
    print(f" - {sc}")
    
'''    