# -*- coding: utf-8 -*-
"""
Created on Sat Apr 4 12:00:35 2026

# Name: query_fdd_on.py

@author: Yimin Chen

# Project Name: FDD-ON ontology development
Copyright (c) 2026 Yimin Chen <chenyimincareer@gmail.com>
Distributed under the terms of the MIT License.

"""

from rdflib import Graph, Namespace
from rdflib.namespace import RDF, RDFS
import numpy as np
import os
import matplotlib
import pandas as pd
from collections import Counter

def count_sub_class (rdf_file_name, upper_class_name):   # Count the number of subclasses
    # %% Load FDD-ON RDF data
    # from rdflib import Graph, Namespace, RDF, RDFS, URIRef

    # 1. Initialize graph and parse the RDF file
    g = Graph()
    print("Loading RDF ontology...")
    g.parse(rdf_file_name, format = "xml")

    # 2. Use SPARQL query to query data (subclass)
    # Using `rdfs:subClassOf+` finds all subclasses transitively (direct and indirect)
    # Replace `rdfs:subClassOf+` with `rdfs:subClassOf` if you ONLY want direct children
    query = f"""
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX ontology: <http://www.semanticweb.org/y6g/ontologies/2025/FDD_ON_VAV_HVAC#>
    
        SELECT DISTINCT ?subclass
        WHERE {{
            ?subclass rdfs:subClassOf+ ontology:{upper_class_name} .
        }}
        """


    '''
    query = """
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        
        SELECT DISTINCT ?subclass
        WHERE {
            ?subclass rdfs:subClassOf+ ?parent .
            FILTER (strends(str(?parent), "AHU-Fault") || strends(str(?parent), "#AHU-Fault"))
           
        }
    """
    '''
    results = g.query(query)
    subclasses = [str(row.subclass) for row in results]
    
    # FILTER (strends(str(?parent), {upper_class_name}}) || strends(str(?parent), {'#'+upper_class_name}))

    print(f"Total subclasses under 'ATU-Fault': {len(subclasses)}\n")
    

    # Extract the section names and component types
    ls_section_name = []
    ls_component_type = []
    for sc in subclasses:
        # Extract fault names
        fault_name = sc.rsplit('#')[1]  
        ls_section_name.append(fault_name)
        
        parts = fault_name.split('-')
        component_type = '-'.join(parts[1:3])   
        ls_component_type.append(component_type)
        
        print(f" - {sc}")
    
    return ls_section_name, ls_component_type


def count_individual (rdf_file_name, upper_class_name):   # Count the number of subclasses

    g = Graph()
    print("Loading RDF ontology...")
    g.parse(rdf_file_name, format="xml")

    # Define SPARQL Query
    # rdfs:subClassOf* recursively includes AHU-Fault and all its subclasses
    query = f"""
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX owl: <http://www.w3.org/2002/07/owl#>
    PREFIX ontology: <http://www.semanticweb.org/y6g/ontologies/2025/FDD_ON_VAV_HVAC#>

    SELECT DISTINCT ?individual ?subclass
    WHERE {{
        ?subclass rdfs:subClassOf+ ontology:{upper_class_name} .
        ?individual a ?subclass .
        ?individual a owl:NamedIndividual .
    }}
    """

    # Execute query
    results = g.query(query)

    individuals = set(row.individual for row in results)

    print(f"\nTotal number of individuals under AHU-Fault subclasses: {len(individuals)}")

    # Optional: Display individual URIs / Names
    ls_individual_name = []
    print("\nList of Individuals:")
    for ind in sorted(individuals):
        # Extract name from the URI
        name = str(ind).split('#')[-1]
        ls_individual_name.append(name)
        print(f" - {name}")
        
    return ls_individual_name


# Load database file
# %% Data file preparation
# Set path
# Input data path
data_path = 'C:\\Users\\...'
data_folder = '...'

rdf_file_name = 'FDD_ON_VAV_HVAC.rdf'
upper_class_name_in = "ImpactLibrary-VAVHVAC-VAVATU"

ls_section_name, ls_component_type = count_sub_class(rdf_file_name, upper_class_name_in)
ls_individual_name = count_individual(rdf_file_name, upper_class_name_in)
    







