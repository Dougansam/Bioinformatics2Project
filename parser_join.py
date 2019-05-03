#!/usr/bin/env python3

'''
-----------------
 EXON MAP PARSER 
-----------------
            
Description:
------------

This program takes a text document containing Genbank records, and, for each record,
returns the first set of 'CDS join' instructions i.e. the instructions describing
how to construct the first-listed (or only) alternatively spliced form of the CDS.

--------------------------------------------------------------------------------
'''
#--------------  
# MAIN PROGRAM
#--------------

import re

# detect & record join instructions
f = open('genbank2.txt','r')
join_found = re.findall(r'ACCESSION[\s]+[A-Z]+[0-9]+.+?FEATURES.+?[\s]+CDS*[\s]*[join]*[\(]*([0-9\s.,]*)',f.read(),re.S)
if join_found != None:
    CDS_maps = join_found

# trim, clean & print join instructions
CDS_maps = [re.sub(r'\s+','', CDS_map) for CDS_map in CDS_maps]
print(CDS_maps,end=',')
print('\n')

# detect, record & print appropriate acc nos 
f = open('genbank2.txt','r')
join_found_acc = re.findall(r'ACCESSION[\s]+([A-Z]+[0-9]+).+?FEATURES.+?[\s]+CDS*[\s]*[join]*[\(]*[0-9\s.,]*',f.read(),re.S)
if join_found_acc != None:
    CDS_maps_acc = join_found_acc
    print(CDS_maps_acc,end=',')
print('\n')

# combine join instructions & print
CDS_maps = CDS_maps + CDS_maps_acc
print(CDS_maps,end=',')
print('\n')

'''
--------------------------------------------------------------------------------
---------------
 KNOWN ISSUES
---------------

None

--------------------------------------------------------------------------------

'''  
