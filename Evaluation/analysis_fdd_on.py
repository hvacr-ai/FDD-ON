# -*- coding: utf-8 -*-
"""
Created on Fri Apr 3 17:49:05 2026

# Name: analysis_fdd_on.py

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


def count_sub_class (file_name, upper_class_name):   # Count the number of subclasses
    # %% Load FDD-ON RDF data
    # from rdflib import Graph, Namespace, RDF, RDFS, URIRef

    # 1. Initialize graph and parse the RDF file
    g = Graph()
    print("Loading RDF ontology...")
    g.parse(file_name, format = "xml")

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

def count_sub_class_method2(file_name, upper_class_name):
       
    # %% Another method to query data. Not use SPARQL
    g = Graph()
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
        
def count_individual (file_name, upper_class_name):   # Count the number of subclasses

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
data_folder = '0...'
fdd_on_file_name = 'System_VAV_HVAC_ATU_2026B' 

data_file_read = os.path.join(data_path, data_folder, fdd_on_file_name) 

rdf_file_name = 'FDD_ON_VAV_HVAC.rdf'
upper_class_name_in = "ImpactLibrary-VAVHVAC-VAVATU"
test_ix = 2

# %% Load database data 
ls_sheet_name = ['Fault library', 'Symptom library', 'Impact library']
df_data_in = pd.read_excel(data_file_read + '.xlsx', sheet_name = ls_sheet_name[test_ix])

# "AHU-Fault", "AHU-Symptom", "ImpactLibrary-VAVHVAC-AHU"
# "VAVATU-Fault", "VAVATU-Symptom", "ImpactLibrary-VAVHVAC-VAVATU"
# "FaultLibrary-VAVHVAC-RTU", "RTU-Symptom", "ImpactLibrary-VAVHVAC-RTU"
# "FaultLibrary-VAVHVAC-CHILLERPLANT", "CHILLERPLANT-Symptom", "ImpactLibrary-VAVHVAC-CHILLERPLANT"
# "FaultLibrary-VAVHVAC-BOILERPLANT", "BOILERPLANT-Symptom", "ImpactLibrary-VAVHVAC-BOILERPLANT"



ls_section_name, ls_component_type = count_sub_class(rdf_file_name, upper_class_name_in)
ls_individual_name = count_individual(rdf_file_name, upper_class_name_in)
    
# %% Compare the RDF output with the database
# Get component types from the 'Component type' column of the database
ls_section = ['Component type', 'Measurement type', 'Component type']

ls_component_type_database_raw = df_data_in[ls_section[test_ix]].tolist()  # Anlayze if there are duplicates in the section in the database

ls_freq_elemt = Counter(ls_component_type_database_raw)

ls_component_type_database = df_data_in[ls_section[test_ix]].unique().tolist()

ls_component_diff = list(set(ls_component_type) ^ set(ls_component_type_database))
    
# %% Compare the RDF output with the database
ls_id_name = ['Fault full ID', 'Symptom full ID', 'Impact full ID']

ls_id_database = df_data_in[ls_id_name[test_ix]].unique().tolist()
ls_id_database_raw = df_data_in[ls_id_name[test_ix]].tolist()

ls_id_diff = list(set(ls_individual_name) ^ set(ls_id_database))

ls_freq_id = Counter(ls_id_database_raw)
