#!/usr/bin/env python3

'''
-----------------------------
 GENBANK DNA SEQUENCE PARSER 
-----------------------------
            
Description:
------------

This program takes a text document containing Genbank records, and returns the
complete DNA sequence taken from each record.

--------------------------------------------------------------------------------
'''
#--------------  
# MAIN PROGRAM
#--------------

import re

# detect & record gene sequences
f = open('genbank2.txt','r')
dna_found = re.findall(r'ORIGIN[\s+]+([a-z\s0-9]+)[\s+]//',f.read())
if dna_found != None:
    dna_seqs = dna_found
    
    # trim, clean & print records
    dna_seqs = [re.sub(r'\s+','', dna_seq) for dna_seq in dna_seqs]
    dna_seqs = [re.sub(r'[0-9]+','', dna_seq) for dna_seq in dna_seqs]
    print(dna_seqs,end=',')
print('\n')

'''
--------------------------------------------------------------------------------
---------------
 KNOWN ISSUES
---------------

None

--------------------------------------------------------------------------------

'''  
