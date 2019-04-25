#!/usr/bin/env python3

'''
--------------------------
 MAIN GENBANK DATA PARSER 
--------------------------
            
Description:
------------
This program takes a text document containing Genbank records and sequentially
returns the data for all records from various key fields. (Fields are: acc_code,
chrom_loc, gene_id, prot_name, gene_span, exon_map, start_cod and complete DNA
sequence.)

--------------------------------------------------------------------------------
'''
#--------------  
# MAIN PROGRAM
#--------------

import re

with open('genbank2.txt','rt') as myfile:
    for line in myfile:
        acc_flag = re.compile('ACCESSION[\s]+([A-Z]+[0-9]+)')
        acc_found = re.match(acc_flag,line)
        if acc_found != None:
            acc_code = acc_found.group(1)
            print(acc_code,end=',')            
print('\n')
with open('genbank2.txt','rt') as myfile:
    for line in myfile:
        gene_flag = re.compile('[\s]+/gene="(.+)"')
        gene_found = re.match(gene_flag,line)
        if gene_found != None:
            gene_id = gene_found.group(1)
            print(gene_id,end=',')
        elif gene_found == None:
            end_flag = re.compile(r'//')
            end_found = re.match(end_flag,line)
            if end_found != None:
                gene_id = 'NF' 
                print(gene_id,end=',')              
print('\n')
with open('genbank2.txt','rt') as myfile:
    for line in myfile:
        prod_flag = re.compile('[\s]+/product="(.+)"')
        prod_found = re.match(prod_flag,line)
        if prod_found != None:
            prot_name = prod_found.group(1)
            print(prot_name,end=',')
        elif prod_found == None:
            end_flag = re.compile(r'//')
            end_found = re.match(end_flag,line)
            if end_found != None:
                prot_name = 'NF' 
                print(prot_name,end=',')        
print('\n')
with open('genbank2.txt','rt') as myfile:
    for line in myfile:
        sour_flag = re.compile('[\s]+source[\s]+((1..)([0-9]+))')
        sour_found = re.match(sour_flag,line)
        if sour_found != None:
            gene_span = sour_found.group(1)
            print(gene_span,end=',')
        elif sour_found == None:
            end_flag = re.compile(r'//')
            end_found = re.match(end_flag,line)
            if end_found != None:
                gene_span = 'NF' 
                print(gene_span,end=',')                
print('\n')
with open('genbank2.txt','rt') as myfile:
    for line in myfile:
        join_flag = re.compile('[\s]+CDS[\s]+(join\()([0-9].+)')
        join_found = re.match(join_flag,line)
        if join_found != None:
            exon_map = join_found.group(2)
            print(exon_map,end='')
        elif join_found == None:
            end_flag = re.compile(r'//')
            end_found = re.match(end_flag,line)
            if end_found != None:
                exon_map = 'NF' 
                print(exon_map,end=',')  
print('\n')            
with open('genbank2.txt','rt') as myfile:
    for line in myfile:
        map_flag = re.compile('[\s]+/map="(.+)"')
        map_found = re.match(map_flag,line)
        if map_found != None:
            chrom_loc = map_found.group(1)
            print(chrom_loc,end=',')
        elif map_found == None:
            end_flag = re.compile(r'//')
            end_found = re.match(end_flag,line)
            if end_found != None:
                map_found = 'NF' 
                print(map_found,end=',')         
print('\n')
with open('genbank2.txt','rt') as myfile:
    for line in myfile: 
        star_flag = re.compile('[\s]+/codon_(start=[1-3])')
        star_found = re.match(star_flag,line)
        if star_found != None:
            start_cod = star_found.group(1)
            print(start_cod,end=',')
        elif star_found == None:
            end_flag = re.compile(r'//')
            end_found = re.match(end_flag,line)
            if end_found != None: 
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
--------------------------------------------------------------------------------
---------------
 KNOWN ISSUES
---------------

Several - still in development

--------------------------------------------------------------------------------

'''  
 

            
