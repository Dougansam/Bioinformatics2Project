#!/usr/bin/env python3

'''
================================================================================
**********************
* GENBANK DNA PARSER *
**********************
            
Description:
------------

This program takes a text document containing Genbank records, and returns the
complete DNA sequence, consecutively, from each record.

'''
#================================================================================
#***************#   
# MAIN PROGRAM  #
#***************#

import re

f = open('genbank2.txt','rt')
dna_found = re.findall\
(r'(ORIGIN)[\s*]+1[\s]([a-z\s0-9]+)[\s]([a-z\s]+)[\s*]([//])',f.read())
if dna_found != None:
    dna_seq = dna_found
    print(dna_seq,end=',')
print('\n')

'''
================================================================================
****************
* KNOWN ISSUES *
****************

1. Currently, output needs trimming to remove extraneous upper case letters,
numbers, white space and brackets.

================================================================================

'''
