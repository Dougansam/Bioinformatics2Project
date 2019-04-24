#!/usr/bin/env python3

'''
================================================================================
****************************
* GENBANK MAIN DATA PARSER *
****************************
            
Description:
------------

This program takes a text document containing Genbank records and sequentially
returns the data for each record from various key fields. (Fields are: acc_code,
chrom_loc, gene_id, prot_name, gene_span, exon_map and start_cod.).

'''
#================================================================================
#***************#   
# MAIN PROGRAM  #
#***************#

import re

new_locus = False
position = 0

with open('genbank2.txt','rt') as myfile:
    for line in myfile:

        loc_flag = re.compile('(LOCUS)')
        loc_found = re.match(loc_flag,line)
        if loc_found != None:
            new_locus = True
            position = position + 1
            map_got = False
            gene_got = False
            prod_got = False
            sour_got = False
            join_got = False
            star_got = False           
            print('LOCUS' ,position, 'of 111:')
        
        acc_flag = re.compile('(ACCESSION)([\s]+)(([A-Z]+)([0-9]+))')
        acc_found = re.match(acc_flag,line)
        if acc_found != None:
            acc_code = acc_found.group(3)
            print(acc_code,end=',')

        if map_got == False:  
            map_flag = re.compile('([\s]+)(/map=")(.+)(")')
            map_found = re.match(map_flag,line)
            if map_found != None:
                map_got = True
                chrom_loc = map_found.group(3)
                print(chrom_loc,end=',')

        if gene_got == False:
            gene_flag = re.compile('([\s]+)(/gene=")(.+)(")')
            gene_found = re.match(gene_flag,line)
            if gene_found != None:
                gene_got = True                
                gene_id = gene_found.group(3)
                print(gene_id,end=',')

        if prod_got == False:
            prod_flag = re.compile('([\s]+)(/product=")(.+)(")')
            prod_found = re.match(prod_flag,line)
            if prod_found != None:
                prod_got = True
                prot_name = prod_found.group(3)
                print(prot_name,end=',')

        if sour_got == False:
            sour_flag = re.compile('(([\s]+)(source)([\s]+))((1..)([0-9]+))')
            sour_found = re.match(sour_flag,line)
            if sour_found != None:
                sour_got = True
                gene_span = sour_found.group(5)
                print(gene_span,end=',')

        if join_got == False:
            join_flag = re.compile('(([\s]+)(CDS)([\s]+))(join\()(([0-9])(.+))')
            join_found = re.match(join_flag,line)
            if join_found != None:
                join_got = True
                exon_map = join_found.group(6)
                print(exon_map,end='')

        if star_got == False:          
            star_flag = re.compile('([\s]+)(/codon_)((start=)([1-3]))')
            star_found = re.match(star_flag,line)
            if star_found != None:
                star_got = True
                start_cod = star_found.group(3)
                print(start_cod,end=',')      

        end_flag = re.compile(r'//')
        end_found = re.match(end_flag,line)
        if end_found != None:
            new_locus = False
            print('\n','NEXT ',end='')

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
