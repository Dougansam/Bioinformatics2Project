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
    exon_maps = join_found

# trim, clean & print join instructions
exon_maps = [re.sub(r'\s+','', exon_map) for exon_map in exon_maps]
print(exon_maps,end=',')
print('\n')

# detect, record & print appropriate acc nos 
f = open('genbank2.txt','r')
join_found_acc = re.findall(r'ACCESSION[\s]+([A-Z]+[0-9]+).+?FEATURES.+?[\s]+CDS*[\s]*[join]*[\(]*[0-9\s.,]*',f.read(),re.S)
if join_found_acc != None:
    exon_maps_acc = join_found_acc
    print(exon_maps_acc,end=',')
print('\n')

# combine join instructions & print
exon_maps = exon_maps + exon_maps_acc
print(exon_maps,end=',')
print('\n')

'''
--------------------------------------------------------------------------------
---------------
 KNOWN ISSUES
---------------

None

--------------------------------------------------------------------------------

'''  
