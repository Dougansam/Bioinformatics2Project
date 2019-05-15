#!/usr/bin/env python3
"""
Program:    
File:       
Version:    V1.0
Date:       07.05.19
Author:     Dr Georgina R Toye 
Address:    Department of Biological Sciences
            School of Science
            Birkbeck College
            University of London
           

================================================================================
***********************
* GENBANK MAIN PARSER *
***********************
            
Description:
------------
This program takes a text document containing Genbank records and sequentially
returns the data for each record from various key fields. Main program returns
the following: acc_code, chrom_loc, gene_id, prot_name, gene_span, and start_cod).
Subprograms below return locus_seq and CDS_map data.
The data is output as a series of MySQL entry statements to populate the table
gb_main

"""
#================================================================================
#***************#   
# MAIN PROGRAM  #
#***************#

import re
position = 0
acc_nums = []
chrom_locs = []
gene_ids = []
prot_names = []
locus_spans = []
gene_spans = []
CDS_spans = []
start_cods = []

with open('genbank.txt','rt') as file:
    for line in file:

        # register start of new record, & count records
        loc_flag = re.compile('(LOCUS)')
        loc_found = re.match(loc_flag,line)
        if loc_found != None:
            position = position + 1
            # optional line (1/2) below to check LOCUS count
            # print('LOCUS' ,position, 'of 111:')

            # reset 'data not found' default for new record            
            locus_span = 'NF'
            chrom_loc = 'NF'
            gene_span = 'NF'
            CDS_span = 'NF'           
            prot_name = 'NF'
            gene_id = 'NF'
            start_cod = 'NF'

            # reset 'data already acquired' flags for new record
            sour_got = False
            map_got = False
            gspan_got = False
            CDS_got = False
            cspan_got = False
            prod_got = False            
            gene_got = False
            star_got = False

        # detect & record specific data types 
        acc_flag = re.compile('ACCESSION[\s]+([A-Z]+[0-9]+)[\s]+')
        acc_found = re.match(acc_flag,line)
        if acc_found != None:
            acc_num = acc_found.group(1)
            acc_nums.append(acc_num)
            
        # avoid possible duplicate data within records
        if sour_got == False:       
            sour_flag = re.compile('[\s]+source[\s]+((1..)([0-9]+))')
            sour_found = re.match(sour_flag,line)
            if sour_found != None:
                sour_got = True     
                locus_span = sour_found.group(1)
                locus_spans.append(locus_span)

        if map_got == False:  
            map_flag = re.compile('[\s]+/map="(.+)"')
            map_found = re.match(map_flag,line)
            if map_found != None:
                map_got = True
                chrom_loc = map_found.group(1)
                chrom_locs.append(chrom_loc)
             
        if gspan_got == False:
            gspan_flag = re.compile('[\s]+gene[\s]+(([0-9]+..)([0-9]+))')
            gspan_found = re.match(gspan_flag,line)
            if gspan_found != None:
                gspan_got = True
                gene_span = gspan_found.group(1)                
                gene_spans.append(gene_span)
                
        # CDS flag reports CDS present, & ensures appropriate data recorded
        if CDS_got == False:
            CDS_flag = re.compile('[gene_\s]+CDS[\s]+')
            CDS_found = re.match(CDS_flag,line)
            if CDS_found != None:
                CDS_got = True
                
        if cspan_got == False:
            cspan_flag = re.compile('[\s]+CDS[\s]+(([0-9]+..)([0-9]+))')
            cspan_found = re.match(cspan_flag,line)
            if cspan_found != None:
                cspan_got = True
                CDS_span = cspan_found.group(1)
                CDS_spans.append(CDS_span)
                
        # CDS flag ensures correct prot_name data reported
        if prod_got == False and CDS_got == True:
            prod_flag = re.compile('[\s]+/product="(.+)"')
            prod_found = re.match(prod_flag,line)
            if prod_found != None:
                prod_got = True
                prot_name = prod_found.group(1)
                prot_names.append(prot_name)
                
        # CDS flag & prod flag ensure correct gene_id data reported     
        if gene_got == False and CDS_got == True and prod_got == False:
            gene_flag = re.compile('[\s]+/gene="(.+)"')
            gene_found = re.match(gene_flag,line)
            if gene_found != None:
                gene_got = True                
                gene_id = gene_found.group(1)
                gene_ids.append(gene_id)

       # CDS flag ensures correct gene_id data reported  
        if star_got == False and CDS_got == True:          
            star_flag = re.compile('[\s]+/codon_(start=[1-3])')
            star_found = re.match(star_flag,line)
            if star_found != None:
                star_got = True
                start_cod = star_found.group(1)     
                start_cods.append(start_cod)
                
        # detect record end; print its data
        end_flag = re.compile(r'//')
        end_found = re.match(end_flag,line)
        if end_found != None:
            if CDS_got == False:
                print("'",acc_num,"'No CDS found',",end='',sep='')
            else:
                print(r'INSERT INTO gb_main VALUES(',end='',sep='')
                print("'",acc_num,"',",end='',sep='')
                print("'",chrom_loc,"',",end='',sep='')
                print("'",gene_id,"',",end='',sep='')
                print("'",prot_name,"',",end='',sep='')
                print("'",locus_span,"',",end='',sep='')
                print("'",gene_span,"',",end='',sep='')
                print("'",CDS_span,"',",end='',sep='')
                print("'",start_cod,"'",end=')\n',sep='')
               # print('\n',end=')\n')
                # optional line (2/2) below to check LOCUS count
                # print('NEXT ',end='')                
print('\n')

'''

#================================================================================
#*****************
# CDS MAP PARSER *
#*****************

Description:
------------

This subprogram takes a text document containing Genbank records and sequentially
returns the data for all records from the cds join(...) field and the accession
number field.

The data is output as a series of MySQL entry statements to populate the table
gb_cds_map

#================================================================================
'''

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

# record, trim & print join instructions
f = open('genbank.txt','r')
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

"""
#================================================================================
#*******************
# LOCUS DNA PARSER *
#*******************
Description:
------------

This subprogram takes a text document containing Genbank records (genbank.txt),
and returns the entire DNA sequence of the locus as a series of MySQL entry
statements. The accession number is also included.

The data is output as a series of MySQL entry statementsto populate the table
gb_seq
================================================================================
"""
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

# record, trim & print DNA sequences
f = open('genbank.txt','r')
orig_found = re.findall(r'ORIGIN[\s+]+([a-z\s0-9]+)[\s+]//',f.read())
if orig_found != None:
    locus_seqs = orig_found
locus_seqs = [re.sub(r'\s+','', locus_seq) for locus_seq in locus_seqs]
locus_seqs = [re.sub(r'[0-9]+','', locus_seq) for locus_seq in locus_seqs]
print('\n')

# combine acc_nos & locus_seqs
gb_seqs = list(zip(acc_nums,locus_seqs))
for gb_seq in gb_seqs:
    print('INSERT INTO gb_seq VALUES',gb_seq,';',end='',sep='')
    print('\n')
'''

================================================================================
****************
* KNOWN ISSUES *
****************

1. There was a problem with record AB043547. This record is 160 820 bp long,
and appeared to cause problems for the MySQL program at the record entry stage.
For this reason, this record was omitted from the database.

2. Some join instructions are not selected despite being present in the
Genbank record. More join instructions could be reported if further work done.

3. complement(location) records not yet dealt with

--------------------------------------------------------------------------------

'''  
