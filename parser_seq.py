#!/usr/bin/env python3

'''
================================================================================
*******************************
* GENBANK GROUPED DATA PARSER *
*******************************
            
Description:
------------

This program takes a text document containing Genbank records and sequentially
returns the data for all records from various key fields. (Fields are: acc_code,
chrom_loc, gene_id, prot_name, gene_span, exon_map, start_cod and complete DNA
sequence.)

'''
#================================================================================
#***************#   
# MAIN PROGRAM  #
#***************#

import re

acc_nums = []

with open('genbank2.txt','rt') as myfile:
    for line in myfile:   
        acc_flag = re.compile('ACCESSION[\s]+([A-Z]+[0-9]+)[\s]+')
        acc_found = re.match(acc_flag,line)
        if acc_found != None:
            acc_num = acc_found.group(1)
            acc_nums.append(acc_num)
#print(acc_nums)
print('\n')

# record, trim & print join instructions
f = open('genbank2.txt','r')
join_found = re.findall(r'ACCESSION[\s]+[A-Z]+[0-9]+.+?FEATURES.+?[\s]+CDS*[\s]*[join]*[\(]*([0-9\s.,]*)',f.read(),re.S)
if join_found != None:
    CDS_maps = join_found
CDS_maps = [re.sub(r'\s+','', CDS_map) for CDS_map in CDS_maps]
#print(CDS_maps,end=',')
print('\n')


# record, trim & print locus DNA sequences
f = open('genbank2.txt','r')
orig_found = re.findall(r'ORIGIN[\s+]+([a-z\s0-9]+)[\s+]//',f.read())
if orig_found != None:
    locus_seqs = orig_found
locus_seqs = [re.sub(r'\s+','', locus_seq) for locus_seq in locus_seqs]
locus_seqs = [re.sub(r'[0-9]+','', locus_seq) for locus_seq in locus_seqs]
#    for locus_seq in locus_seqs:
#    print("'",'5',"'",end=',',sep='')
#print(locus_seqs,end=',')
print('\n')

gb_seq = list(zip(acc_nums,CDS_maps,locus_seqs))
print(gb_seq)

'''
================================================================================
****************
* KNOWN ISSUES *
****************

1. For loci containing a partial cds followed by a complete cds, the
program will provide the product of the partial sequence and the gene id of
the complete sequence. This needs fixing.

2. Some join instructions are not selected despite being present in the
Genbank record. This is due to non-standard methods of listing by submitters.
More join instructions could be reported if further work was done.

3. The 'NF' = 'record not found' utility needs to be added to this program.

================================================================================

'''
 

            
