#!/usr/bin/env python3

'''
--------------------------
 MAIN GENBANK DATA PARSER 
--------------------------
            
Description:
------------
This program takes a text document containing Genbank records and sequentially
returns the data for each record from various key fields (acc_code, chrom_loc,
gene_id, prot_name, gene_span, and start_cod).

--------------------------------------------------------------------------------
'''
#--------------  
# MAIN PROGRAM
#--------------

import re
position = 0

with open('genbank2.txt','rt') as file:
    for line in file:
        
        # register start of new record, & count records
        loc_flag = re.compile('(LOCUS)')
        loc_found = re.match(loc_flag,line)
        if loc_found != None:
            position = position + 1
            print('LOCUS' ,position, 'of 111:')

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
            
        # avoid possible duplicate data within records
        if sour_got == False:       
            sour_flag = re.compile('[\s]+source[\s]+((1..)([0-9]+))')
            sour_found = re.match(sour_flag,line)
            if sour_found != None:
                sour_got = True     
                locus_span = sour_found.group(1)

        if map_got == False:  
            map_flag = re.compile('[\s]+/map="(.+)"')
            map_found = re.match(map_flag,line)
            if map_found != None:
                map_got = True
                chrom_loc = map_found.group(1)
            
        if gspan_got == False:
            gspan_flag = re.compile('[\s]+gene[\s]+(([0-9]+..)([0-9]+))')
            gspan_found = re.match(gspan_flag,line)
            if gspan_found != None:
                gspan_got = True
                gene_span = gspan_found.group(1)                
                
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
                
        # CDS flag ensures correct prot_name data reported
        if prod_got == False and CDS_got == True:
            prod_flag = re.compile('[\s]+/product="(.+)"')
            prod_found = re.match(prod_flag,line)
            if prod_found != None:
                prod_got = True
                prot_name = prod_found.group(1)
                
        # CDS flag & prod flag ensure correct gene_id data reported     
        if gene_got == False and CDS_got == True and prod_got == False:
            gene_flag = re.compile('[\s]+/gene="(.+)"')
            gene_found = re.match(gene_flag,line)
            if gene_found != None:
                gene_got = True                
                gene_id = gene_found.group(1)

       # CDS flag ensures correct gene_id data reported  
        if star_got == False and CDS_got == True:          
            star_flag = re.compile('[\s]+/codon_(start=[1-3])')
            star_found = re.match(star_flag,line)
            if star_found != None:
                star_got = True
                start_cod = star_found.group(1)     

        # detect record end; print its data
        end_flag = re.compile(r'//')
        end_found = re.match(end_flag,line)
        if end_found != None:
            if CDS_got == False:
                print(acc_num,'No CDS found')
            else:
                print(acc_num,end=',')
                print(chrom_loc,end=',')
                print(gene_id,end=',')
                print(prot_name,end=',')
                print(locus_span,end=',')
                print(gene_span,end=',')
                print(CDS_span,end=',')
                print(start_cod,end=',') 
                print('\n','NEXT ',end='')
print('\n')

'''
--------------------------------------------------------------------------------
---------------
 KNOWN ISSUES
---------------

1. Some join instructions not selected
2. Report CDS_span if no CDS_map instructions
3. complement(location) records need doing

--------------------------------------------------------------------------------

'''  
