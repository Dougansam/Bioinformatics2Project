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
returns the data for each record from various key fields (acc_code, chrom_loc,
gene_id, prot_name, gene_span, and start_cod).

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

with open('genbank2.txt','rt') as file:
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

--------------------------------------------------------------------------------
---------------
 KNOWN ISSUES
---------------

1. Some join instructions not selected
2. complement(location) records not yet dealt with

--------------------------------------------------------------------------------

'''  
