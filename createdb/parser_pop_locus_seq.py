#!/usr/bin/env python3

'''
----------------------
LOCUS SEQUENCE PARSER 
----------------------
   
        
Description:
------------
This program takes a text document containing Genbank records (genbank.txt),
and returns the entire DNA sequence of the locus as a series of MySQL entry
statements. The accession number is also included.
--------------------------------------------------------------------------------
'''
#--------------  
# MAIN PROGRAM
#--------------

import re

# detect & record accession numbers
acc_nums = []
with open('genbank.txt','rt') as myfile:
    for line in myfile:   
        acc_flag = re.compile('ACCESSION[\s]+([A-Z]+[0-9]+)[\s]+')
        acc_found = re.match(acc_flag,line)
        if acc_found != None:
            acc_num = acc_found.group(1)
            acc_nums.append(acc_num)
print('\n')

# detect & record locus DNA sequences
f = open('genbank.txt','r')
orig_found = re.findall(r'ORIGIN[\s+]+([a-z\s0-9]+)[\s+]//',f.read())
if orig_found != None:
    locus_seqs = orig_found
    
# trim, clean & print locus DNA sequences
locus_seqs = [re.sub(r'\s+','', locus_seq) for locus_seq in locus_seqs]
locus_seqs = [re.sub(r'[0-9]+','', locus_seq) for locus_seq in locus_seqs]
#print(locus_seqs,end=',')
print('\n')

# combine acc_nos & locus_seqs
gb_seqs = list(zip(acc_nums,locus_seqs))
for gb_seq in gb_seqs:
    print('INSERT INTO gb_seq VALUES',gb_seq,';',end='',sep='')
    print('\n')
'''
--------------------------------------------------------------------------------
---------------
 KNOWN ISSUES
---------------
None
--------------------------------------------------------------------------------
''' 
