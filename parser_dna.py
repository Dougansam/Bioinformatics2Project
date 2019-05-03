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

# detect & record locus DNA sequences
f = open('genbank2.txt','r')
orig_found = re.findall(r'ORIGIN[\s+]+([a-z\s0-9]+)[\s+]//',f.read())
if orig_found != None:
    locus_seqs = orig_found
    
# trim, clean & print locus DNA sequences
locus_seqs = [re.sub(r'\s+','', locus_seq) for locus_seq in locus_seqs]
locus_seqs = [re.sub(r'[0-9]+','', locus_seq) for locus_seq in locus_seqs]
print(locus_seqs,end=',')
print('\n')

'''
--------------------------------------------------------------------------------
---------------
 KNOWN ISSUES
---------------

None

--------------------------------------------------------------------------------

'''  
