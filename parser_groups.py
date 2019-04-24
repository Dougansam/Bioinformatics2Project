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

with open('genbank2.txt','rt') as myfile:
    for line in myfile:   
        acc_flag = re.compile('(ACCESSION)([\s]+)(([A-Z]+)([0-9]+))')
        acc_found = re.match(acc_flag,line)
        if acc_found != None:
            acc_code = acc_found.group(3)
            print(acc_code,end=',')
print('\n')            
with open('genbank2.txt','rt') as myfile:
    for line in myfile:   
        map_flag = re.compile('([\s]+)(/map=")(.+)(")')
        map_found = re.match(map_flag,line)
        if map_found != None:
            chrom_loc = map_found.group(3)
            print(chrom_loc,end=',')
print('\n')
with open('genbank2.txt','rt') as myfile:
    for line in myfile:
        gene_flag = re.compile('([\s]+)(/gene=")(.+)(")')
        gene_found = re.match(gene_flag,line)
        if gene_found != None:
            gene_id = gene_found.group(3)
            print(gene_id,end=',')
print('\n')
with open('genbank2.txt','rt') as myfile:
    for line in myfile:
        prod_flag = re.compile('([\s]+)(/product=")(.+)(")')
        prod_found = re.match(prod_flag,line)
        if prod_found != None:
            prot_name = prod_found.group(3)
            print(prot_name,end=',')
print('\n')
with open('genbank2.txt','rt') as myfile:
    for line in myfile:
        sour_flag = re.compile('(([\s]+)(source)([\s]+))((1..)([0-9]+))')
        sour_found = re.match(sour_flag,line)
        if sour_found != None:
            gene_span = sour_found.group(5)
            print(gene_span,end=',')
print('\n')
with open('genbank2.txt','rt') as myfile:
    for line in myfile:
        join_flag = re.compile('(([\s]+)(CDS)([\s]+))(join\()(([0-9])(.+))')
        join_found = re.match(join_flag,line)
        if join_found != None:
            exon_map = join_found.group(6)
            print(exon_map,end='')
print('\n')
with open('genbank2.txt','rt') as myfile:
    for line in myfile:
        star_flag = re.compile('([\s]+)(/codon_)((start=)([1-3]))')
        star_found = re.match(star_flag,line)
        if star_found != None:
            start_cod = star_found.group(3)
            print(start_cod,end=',')
print('\n')
f = open('genbank2.txt','r')
dna_found = re.findall(r'ORIGIN[\s*]+([a-z\s0-9]+)[\s*]//',f.read())
if dna_found != None:
    dna_seqs = dna_found
    dna_seqs = [re.sub(r'\s+','', dna_seq) for dna_seq in dna_seqs]
    dna_seqs = [re.sub(r'[0-9]+','', dna_seq) for dna_seq in dna_seqs]
    print(dna_seqs,end=',')
print('\n')

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
 

            