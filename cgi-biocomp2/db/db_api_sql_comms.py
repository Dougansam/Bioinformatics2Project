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
           
-------------------------------------------------------------------------------

---------------
 DATABASE API 
---------------
            
Description:
------------

1. String searches:
The program takes a 'search' data field descriptor (1 -4), a search string, and
an 'output' data field/s descriptor (1-8). It returns data from requested output
field/s for any matching record/s.

2. Browse requests:
The program takes a 'browse' data field descriptor (1-8), a 'browse data field/s'
request string 'B', and an 'additional output' data field/s descriptor. It returns
data for ALL records from stipulated browse fields AND, where different,
stipulated output field/s.

================================================================================
"""
#---------------------
# FUNCTION db_request 
#---------------------

def db_request(db_input, db_query, db_output):
    
    '''Return specified DB record/s, via string search or browse request.
    String searches:
    Input:  db_input..........................The data field to be searched
            db_query..........................The string to be searched for
            db_output.......................The data field/s to be returned
    Output: db_result......Data from relevant field/s for matching record/s 
    Browse requests:   
    Input:  db_input................A data field to be browsed AND returned
            db_query........................The 'browse data field' request
            db_output.......Optional additional data field/s to be returned
    Output: db_result...........Data from relevant field/s for ALL record/s
    '''
    
    db_result = []
    db_input_result = []

    
    # data for unique string searches on acc_no
    if db_query != 'B' and db_input == 1:
        
        if db_output == 1: 
            # data_acc_num
            db_result = "SELECT acc_num FROM gb_main WHERE acc_num LIKE "
        elif db_output == 2:
            # data_chrom_loc
            db_result = "SELECT chrom_loc, acc_num FROM gb_main WHERE acc_num LIKE "
        elif db_output == 3:
            # data_gene_id
            db_result = "SELECT gene_id, acc_num FROM gb_main WHERE acc_num LIKE "
        elif db_output == 4:
            # data_prot_name
            db_result = "SELECT prot_name, acc_num FROM gb_main WHERE acc_num LIKE "
        elif db_output == 5:
            # data_locus_seq
            db_result = "SELECT locus_seq, acc_num FROM gb_seq WHERE acc_num LIKE "
        elif db_output == 6:
            # data_CDS_map
            db_result = "SELECT cds_map,start_cod,gene_span,gb_main.acc_num\
                        FROM gb_main\
                        INNER JOIN gb_cds_map\
                        ON gb_main.acc_num = gb_cds_map.acc_num\
                        WHERE gb_main.acc_num LIKE "
        elif db_output == 7:
            # data_list_short
            db_result = "SELECT acc_num, chrom_loc, gene_id, prot_name\
                        FROM gb_main\
                        WHERE acc_num LIKE "
        elif db_output == 8:
            # data_list_long
            db_result = "SELECT m.acc_num, chrom_loc, gene_id, prot_name, locus_seq, cds_map,\
                        start_cod, gene_span\
                        FROM gb_main m, gb_seq s, gb_cds_map c\
                        WHERE s.acc_num = m.acc_num\
                        AND c.acc_num = m.acc_num\
                        AND m.acc_num LIKE "

        return db_result

    # data for non-unique string searches on chrom_loc
    if db_query != 'B':
        if db_input == 2:
                
            if db_output == 1: 
                # data_acc_codes
                db_result = "SELECT acc_num FROM gb_main WHERE chrom_loc LIKE "
            elif db_output == 2:
                # data_chrom_locs
                db_result = "SELECT chrom_loc, acc_num FROM gb_main WHERE chrom_loc LIKE "
            elif db_output == 3:
                # data_gene_ids
                db_result = "SELECT gene_id, acc_num FROM gb_main WHERE chrom_loc LIKE "
            elif db_output == 4:
                # data_prot_names
                db_result = "SELECT prot_name, acc_no FROM gb_main WHERE chrom_loc LIKE "
            elif db_output == 5:
                # data_locus_seqs
                db_result = "SELECT locus_seq,gb_main.acc_num FROM gb_main INNER JOIN gb_seq\
                            ON gb_main.acc_num = gb_seq.acc_num\
                            WHERE chrom_loc LIKE "
            elif db_output == 6:
                # data_CDS_maps
                db_result = "SELECT cds_map,start_cod,gene_span,gb_main.acc_num\
                            FROM gb_main INNER JOIN gb_cds_map ON gb_main.acc_num = gb_cds_map.acc_num\
                            WHERE chrom_loc LIKE "
            elif db_output == 7:
                # data_lists_short
                db_result = "SELECT acc_num, chrom_loc, gene_id, prot_name\
                             FROM gb_main WHERE chrom_loc LIKE "
            elif db_output == 8:
                # data_lists_long
                db_result = "SELECT m.acc_num, chrom_loc, gene_id, prot_name, locus_seq, cds_map, start_cod, gene_span\
                             FROM gb_main m, gb_seq s, gb_cds_map c\
                             WHERE s.acc_num = m.acc_num AND c.acc_num = m.acc_num AND chrom_loc LIKE "
            return db_result

 # data for non-unique string searches on gene_id
        if db_query != 'B':
            if db_input == 3:
                
                if db_output == 1: 
                    # data_acc_codes
                    db_result = "SELECT acc_num FROM gb_main WHERE gene_id LIKE "
                elif db_output == 2:
                    # data_chrom_locs
                    db_result = "SELECT chrom_loc, acc_num FROM gb_main WHERE gene_id LIKE "
                elif db_output == 3:
                    # data_gene_ids
                    db_result = "SELECT gene_id, acc_num FROM gb_main WHERE gene_id LIKE "
                elif db_output == 4:
                    # data_prot_names
                    db_result = "SELECT prot_name, acc_no FROM gb_main WHERE gene_id LIKE "
                elif db_output == 5:
                    # data_locus_seqs
                    db_result = "SELECT locus_seq,gb_main.acc_num FROM gb_main\
                                 INNER JOIN gb_seq ON gb_main.acc_num = gb_seq.acc_num\
                                 WHERE gene_id LIKE "
                elif db_output == 6:
                    # data_CDS_maps
                    db_result = "SELECT cds_map,start_cod,gene_span,gb_main.acc_num\
                                 FROM gb_main INNER JOIN gb_cds_map ON gb_main.acc_num = gb_cds_map.acc_num\
                                 WHERE gene_id LIKE "
                elif db_output == 7:
                    # data_lists_short
                    db_result = "SELECT acc_num,chrom_loc,gene_id,prot_name\
                                 FROM gb_main WHERE gene_id LIKE "
                elif db_output == 8:
                    # data_lists_long
                    db_result = "SELECT m.acc_num, chrom_loc, gene_id, prot_name, locus_seq, cds_map, start_cod, gene_span\
                                 FROM gb_main m, gb_seq s, gb_cds_map c\
                                 WHERE s.acc_num = m.acc_num AND c.acc_num = m.acc_num AND gene_id LIKE "
                return db_result

 # data for non-unique string searches on prot_name
        if db_query != 'B':
            if db_input == 4:
                
                if db_output == 1: 
                    # data_acc_codes
                    db_result = "SELECT acc_num FROM gb_main WHERE prot_name LIKE "
                elif db_output == 2:
                    # data_chrom_locs
                    db_result = "SELECT chrom_loc, acc_num FROM gb_main WHERE prot_name LIKE "
                elif db_output == 3:
                    # data_gene_ids
                    db_result = "SELECT gene_id, acc_num FROM gb_main WHERE prot_name LIKE "
                elif db_output == 4:
                    # data_prot_names
                    db_result = "SELECT prot_name, acc_no FROM gb_main WHERE prot_name LIKE "
                elif db_output == 5:
                    # data_locus_seqs
                    db_result = "SELECT locus_seq,gb_main.acc_num FROM gb_main\
                                 INNER JOIN gb_seq ON gb_main.acc_num = gb_seq.acc_num\
                                 WHERE prot_name LIKE "
                    # data_CDS_maps
                    db_result = "SELECT cds_map,start_cod,gene_span,gb_main.acc_num\
                                 FROM gb_main INNER JOIN gb_cds_map ON gb_main.acc_num = gb_cds_map.acc_num\
                                 WHERE prot_name LIKE "
                elif db_output == 7:
                    # data_lists_short
                    db_result = "SELECT acc_num, chrom_loc, gene_id, prot_name\
                                 FROM gb_main WHERE prot_name LIKE "
                elif db_output == 8:
                    # data_lists_long
                    db_result = "SELECT m.acc_num, chrom_loc, gene_id, prot_name, locus_seq, cds_map, start_cod, gene_span\
                                 FROM gb_main m, gb_seq s, gb_cds_map c\
                                 WHERE s.acc_num = m.acc_num AND c.acc_num = m.acc_num AND prot_name LIKE "
                return db_result


    # data for browsing input categories 
    if db_query == 'B':

        if db_input == 1:
            if db_output == 1:
                db_result = "SELECT acc_num FROM gb_main"
            elif db_output == 2:
                db_result = "SELECT acc_num,chrom_loc FROM gb_main"
            elif db_output == 3:
                db_result = "SELECT acc_num, gene_id, FROM gb_main"
            elif db_output == 4:
                db_result = "SELECT acc_num, prot_name FROM gb_main"

        elif db_input == 2:
            if db_output == 1:
                db_result = "SELECT chrom_loc,acc_num FROM gb_main"
            elif db_output == 2:
                db_result = "SELECT chrom_loc,acc_num FROM gb_main"
            elif db_output == 3:
                db_result = "SELECT chrom_loc, gene_id, acc_num FROM gb_main"
            elif db_output == 4:
                db_result = "SELECT chrom_loc, prot_name, acc_no FROM gb_main"

        elif db_input == 3:
            if db_output == 1:
                db_result = "SELECT gene_id, acc_num FROM gb_main"
            elif db_output == 2:
                db_result = "SELECT gene_id, chrom_loc, acc_num FROM gb_main;"
            elif db_output == 3:
                db_result = "SELECT gene_id, acc_num FROM gb_main"
            elif db_output == 4:
                db_result = "SELECT gene_id, prot_name, acc_num FROM gb_main"
                
        elif db_input == 4:
            if db_output == 1:
                db_result = "SELECT prot_name, acc_num FROM gb_main;"
            elif db_output == 2:
                db_result = "SELECT prot_name, chrom_loc, acc_num FROM gb_main"
            elif db_output == 3:
                db_result = "SELECT prot_name, gene_id, acc_num FROM gb_main;"
            elif db_output == 4:
                db_result = "SELECT prot_name, acc_num FROM gb_main;"

    return db_result

'''
--------------------------------------------------------------------------------
'''
#--------------  
# MAIN PROGRAM
#--------------


db_input = []
db_query = []
db_output = []

db_result = []

db_input = int(input("Enter data input category for search (1-4) or \
browse (1-8): "))

db_query = str(input("Enter a search term string for the \
selected category, or enter 'B' to browse a category: "))

if db_query != 'B':
    if db_input < 1 or db_input > 4:
        print("String search: data category error")
else:
    if db_input < 1 or db_input > 8:
        print("Browse: data category error")
        
db_output = int(input("Enter output data category (1-8): "))

if db_output < 1 or db_output > 8:
        print("Output data category error")

db_result = db_request(db_input, db_query, db_output)


# Print appropriate MySQL request
if db_query == 'B': 
    print("Database request results:")
    print(db_result, db_query, end='',sep='')

else:
    print("Database request results:")
    print(db_result, "%", db_query, "%", end='',sep='')

'''      
--------------------------------------------------------------------------------
---------------
 KNOWN ISSUES
---------------

1. Need to convert to automatic rather than manual entry of parameters.
2. Some options given in this dummy program should be made not available in the
final db_api due to excessive size of the output records e.g it should not be
possible to browse all DNA sequence records.

--------------------------------------------------------------------------------

'''
