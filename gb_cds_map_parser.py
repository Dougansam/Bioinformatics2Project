#!/usr/bin/env python3

'''
================================================================================
**************************
* GENBANK CDS MAP PARSER *
**************************
            
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

# detect & record accession numbers
acc_nums = []
with open('genbank2.txt','rt') as myfile:
    for line in myfile:   
        acc_flag = re.compile('ACCESSION[\s]+([A-Z]+[0-9]+)[\s]+')
        acc_found = re.match(acc_flag,line)
        if acc_found != None:
            acc_num = acc_found.group(1)
            acc_nums.append(acc_num)
print('\n')

# record, trim & print join instructions
f = open('genbank2.txt','r')
join_found = re.findall(r'ACCESSION[\s]+[A-Z]+[0-9]+.+?FEATURES.+?[\s]+CDS*[\s]*[join]*[\(]*([0-9\s.,]*)',f.read(),re.S)
if join_found != None:
    cds_maps = join_found
cds_maps = [re.sub(r'\s+','', cds_map) for cds_map in cds_maps]
print('\n')

# combine acc_nos & cds_maps
gb_cds_maps = list(zip(acc_nums,cds_maps))
for gb_cds_map in gb_cds_maps:
    print('INSERT INTO gb_cds_map VALUES',gb_cds_map,';',end='',sep='')
    print('\n')

'''
================================================================================
****************
* KNOWN ISSUES *
****************

1. Some join instructions are not selected despite being present in the
Genbank record. More join instructions could be reported if further work done.

================================================================================

'''
 

            
