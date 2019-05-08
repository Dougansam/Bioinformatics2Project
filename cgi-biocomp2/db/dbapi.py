#!/usr/bin/env python3

'''OLD VERSION INCLUDED FOR USE WITH BL - GRToye
---------------
 DATABASE API 
---------------
            
Description:
------------

1. String searches:
The program takes a 'search' data field descriptor, a search
string, and an 'output' data field/s descriptor. It returns data from requested
output field/s for any matching record/s.
2. Browse requests:
The program takes a 'browse' data field descriptor, a 'browse data field'
request, and an 'additional output' data field/s descriptor. It returns data
for ALL records from stipulated browse fields AND, where different,
stipulated output field/s.

================================================================================
'''
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
    
    # data for unique string searches 
    if db_query != 'B' and db_input == 1:
        
        if db_output == 1: 
            # data_acc_num
            db_result = [['AF485254']]
        elif db_output == 2:
            # data_chrom_loc
            db_result = [['18q24.3'],['U55184']]
        elif db_output == 3:
            # data_gene_id
            db_result = [['NPC1'],['U11424']]
        elif db_output == 4:
            # data_prot_name
            db_result = [['desmoglein type 1'],['AJ001716']]
        elif db_output == 5:
            # data_locus_seq
            db_result = [['gtaagtatcttagcgtcattttctactatgacctgagggttgctac'],\
                        ['U19568']]
        elif db_output == 6:
            # data_CDS_map
            db_result = [['179..5187,6619..7050'],['start=1'],['24..8876'],\
                         ['D00596']]
        elif db_output == 7:
            # data_list_short
            db_result = [['D00596'],['18q24'],['TPMT'],['desmoglein type 1']]
        elif db_output == 8:
            # data_list_long
            db_result = [['U11424'],['18q11.2'],['DSG1'],\
                        ['desmoglein type 1'],\
                        ['caccttctactatgacctgagggttgctacatcacccaccac'],\
                        ['179..5187,6619..7050'],['start=3'],['24..8876']]
        return db_result

    # data for non-unique string searches
    if db_query != 'B':
        if db_input == 2 or db_input == 3 or db_input == 4:
                
            if db_output == 1: 
                # data_acc_codes
                db_result = [['AF485254'],['AF485254'],\
                            ['AF485254'],['AF485254']]
            elif db_output == 2:
                # data_chrom_locs
                db_result = [['18q24.3','18q24'],['AF485254','U49845']]
            elif db_output == 3:
                # data_gene_ids
                db_result = [['NPC1','NPC1R','pseudoNPC1a'],\
                            ['AF485254','U49845','AF165912']]
            elif db_output == 4:
                # data_prot_names
                db_result = \
                [['desmoglein type 1','desmoglein 4 preproprotein'],\
                ['AF485254','U49845']]
            elif db_output == 5:
                # data_locus_seqs
                db_result = \
                [['gtaagtatcttagcgtcattttctactatgacctgagggttgctac'],\
                ['AF485254'],['gtaagtatcttagcgtcattt'],['U19568']]
            elif db_output == 6:
                # data_CDS_maps
                db_result = [['179..5187,6619..7050'],\
                ['start=2'],['24..8876'],['AF485254']]
            elif db_output == 7:
                # data_lists_short
                db_result = [['D00596','U11424'],\
                ['18q24','18q24'],['TPMT','pseudoTPMT'],\
                ['desmoglein type 1','desmoglein 4 preproprotein']]
            elif db_output == 8:
                # data_lists_long
                db_result = [['D00596','U11424'],['18q24','18q24'],
                ['TPMT','pseudoTPMT'],\
                ['desmoglein type 1','desmoglein 4 preproprotein'],\
                ['cacccacatataacccaatgtatttataatttgtcgtgtcgatcacccaccac',\
                'tcttagaaggtatcttagcgtcattttctactacctatatataacaatgacaac'],\
                ['99..187,300..490,6619..7050','159..1187,1200..5079'],\
                ['start=1','start=3'],['22..7953','103,6012']]
            return db_result
    
    # data for browsing input categories 
    if db_query == 'B':
        if db_input != db_output:
        
            if db_input == 1:
                # list_acc_codes
                db_input_result = [[['AF485251','U49845','U19576', 'U55184',\
                'AF165912','AJ001716'],['AF485251','U49845','U19576', 'U55184',\
                'AF165912','AJ001716']]]
            elif db_input == 2:
                # list_chrom_locs
                db_input_result = [[['18q24.3','18q24','18q24','18q11.2',\
                'q12.1','18q11'],['AF485251','U49845','U19576', 'U55184',\
                'AF165912','AJ001716']]]
            elif db_input == 3:
                # list_gene_ids
                db_input_result = [[['NPC1','TPMT','pseudoTPMT','DSG1',\
                'DSG1','SALL3'],['AF485251','U49845','U19576', 'U55184',\
                'AF165912','AJ001716']]]
            elif db_input == 4:
                # list_prot_names
                db_input_result = [[['Niemann-Pick C1 disease protein',\
                'Niemann-Pick C1 disease protein receptor',\
                'desmoglein type 1','desmoglein 4 preproprotein',\
                'spalt-like zinc finger protein','ferrochelatase'],\
                ['AF485251','U49845','U19576','U55184','AF165912','AJ001716']]]
            elif db_input == 5:
                # list_locus_seqs
                db_input_result = [[['cacccacataacatataacatattcgtaacctcacacc',\
                'tcttagaaggtatcttagcgtcattttctactacctatatataatgggtttgactaaac',\
                'aggactcatacactacacatacacatataacatatttcttttattaacatgtatttctt',\
                'ggttagaaggtatcttagcgtcattttcatatataacatgaccttgggtttgactaaac',\
                'ctgactcatacaccacatataacatattatataacatcttttattaacatgtatttctt',\
                'tatatccaggatatattttgctttgtcgatcacttacctaatattaaactgatgccat'],\
                ['AF485251','U49845','U19576','U55184','AF165912','AJ001716']]]
            elif db_input == 6:
                # list_CDS_maps
                db_input_result = [[['179..5187,6619..7050','NF',\
                '99..587,619..1150','111..183,8360..8395, 11591..11746',\
                '159..1187,1200..5079','8360..8395,9912..10043'],
                ['start=1','start=1','start=2','start=1','start=3','start=1'],\
                ['22..7953','103,6012','21..1234',\
                '32..13123','55..6023','8099..11034'],
                ['AF485251','U49845','U19576','U55184','AF165912','AJ001716']]]
            elif db_input == 7:      
                # data_lists_short
                db_input_result = [[['AF485251','U49845','U19576','U55184',\
                'AF165912','AJ001716'],['18q24.3','18q24','18q24','18q11.2',\
                'q12.1','18q11'],['NPC1','TPMT','pseudoTPMT','DSG1','DSG1',\
                'SALL3'],['Niemann-Pick C1 disease protein',\
                'Niemann-Pick C1 disease protein receptor','desmoglein type 1',\
                'desmoglein 4 preproprotein','spalt-like zinc finger protein',\
                'ferrochelatase']]]
            elif db_input == 8:
                # data_lists_long
                db_input_result = [[['AF485251','U49845','U19576','U55184',\
                'AF165912','AJ001716'],['18q24.3','18q24','18q24','18q11.2',\
                'q12.1','18q11'],['NPC1','TPMT','pseudoTPMT','DSG1','DSG1',\
                'SALL3'],['Niemann-Pick C1 disease protein',\
                'Niemann-Pick C1 disease protein receptor','desmoglein type 1',\
                'desmoglein 4 preproprotein','spalt-like zinc finger protein',\
                'ferrochelatase'],['cacccacataacatataacatattcgtaacctcacacc',\
                'tcttagaaggtatcttagcgtcattttctactacctatatataatgggtttgactaaac',\
                'aggactcatacactacacatacacatataacatatttcttttattaacatgtatttctt',\
                'ggttagaaggtatcttagcgtcattttcatatataacatgaccttgggtttgactaaac',\
                'ctgactcatacaccacatataacatattatataacatcttttattaacatgtatttctt',\
                'tatatccaggatatattttgctttgtcgatcacttacctaatattaaactgatgccat'],\
                ['179..5187,6619..7050','NF','99..587,619..1150',\
                '111..183,8360..8395,11591..11746','159..1187,1200..5079',\
                '8360..8395,9912..10043'],['start=1','start=1','start=2',\
                'start=1','start=3','start=1'],['22..7953','103,6012',\
                '21..1234','32..13123','55..6023','8099..11034']]]  

        # data for browsing additional output categories
        if db_output == 1:
            # list_acc_codes
            db_result = [['AF485251','U49845','U19576','U55184','AF165912',\
            'AJ001716'],['AF485251','U49845','U19576', 'U55184','AF165912',\
            'AJ001716']]    
        elif db_output == 2:
             # list_chrom_locs
            db_result = [['18q24.3','18q24','18q24','18q11.2',\
                'q12.1','18q11'],['AF485251','U49845','U19576', 'U55184',\
                'AF165912','AJ001716']]
        elif db_output == 3:
            # list_gene_ids
            db_result = [['NPC1','TPMT','pseudoTPMT','DSG1',\
                'DSG1','SALL3'],['AF485251','U49845','U19576', 'U55184',\
                'AF165912','AJ001716']]
        elif db_output == 4:
            # list_prot_names
            db_result = [['Niemann-Pick C1 disease protein',\
                'Niemann-Pick C1 disease protein receptor',\
                'desmoglein type 1','desmoglein 4 preproprotein',\
                'spalt-like zinc finger protein','ferrochelatase'],\
                ['AF485251','U49845','U19576','U55184','AF165912','AJ001716']]
        elif db_output == 5:
            # list_locus_seqs
            db_result = [['cacccacataacatataacatattcgtaacctcacacc',\
                'tcttagaaggtatcttagcgtcattttctactacctatatataatgggtttgactaaac',\
                'aggactcatacactacacatacacatataacatatttcttttattaacatgtatttctt',\
                'ggttagaaggtatcttagcgtcattttcatatataacatgaccttgggtttgactaaac',\
                'ctgactcatacaccacatataacatattatataacatcttttattaacatgtatttctt',\
                'tatatccaggatatattttgctttgtcgatcacttacctaatattaaactgatgccat'],\
                ['AF485251','U49845','U19576','U55184','AF165912','AJ001716']]
        elif db_output == 6:
            # list_CDS_maps
            db_result = [['179..5187,6619..7050','NF',\
                '99..587,619..1150','111..183,8360..8395, 11591..11746',\
                '159..1187,1200..5079','8360..8395,9912..10043'],
                ['start=1','start=1','start=2','start=1','start=3','start=1'],\
                ['22..7953','103,6012','21..1234',\
                '32..13123','55..6023','8099..11034'],         
                ['AF485251','U49845','U19576','U55184','AF165912','AJ001716']]
        elif db_output  == 7:      
            # data_lists_short
            db_result = [['AF485251','U49845','U19576','U55184',\
                'AF165912','AJ001716'],['18q24.3','18q24','18q24','18q11.2',\
                'q12.1','18q11'],['NPC1','TPMT','pseudoTPMT','DSG1','DSG1',\
                'SALL3'],['Niemann-Pick C1 disease protein',\
                'Niemann-Pick C1 disease protein receptor','desmoglein type 1',\
                'desmoglein 4 preproprotein','spalt-like zinc finger protein',\
                'ferrochelatase']]
        elif db_output == 8:
            # data_lists_long
            db_result = [['AF485251','U49845','U19576','U55184',\
                'AF165912','AJ001716'],['18q24.3','18q24','18q24','18q11.2',\
                'q12.1','18q11'],['NPC1','TPMT','pseudoTPMT','DSG1','DSG1',\
                'SALL3'],['Niemann-Pick C1 disease protein',\
                'Niemann-Pick C1 disease protein receptor','desmoglein type 1',\
                'desmoglein 4 preproprotein','spalt-like zinc finger protein',\
                'ferrochelatase'],['cacccacataacatataacatattcgtaacctcacacc',\
                'tcttagaaggtatcttagcgtcattttctactacctatatataatgggtttgactaaac',\
                'aggactcatacactacacatacacatataacatatttcttttattaacatgtatttctt',\
                'ggttagaaggtatcttagcgtcattttcatatataacatgaccttgggtttgactaaac',\
                'ctgactcatacaccacatataacatattatataacatcttttattaacatgtatttctt',\
                'tatatccaggatatattttgctttgtcgatcacttacctaatattaaactgatgccat'],\
                ['179..5187,6619..7050','NF','99..587,619..1150',\
                '111..183,8360..8395,11591..11746','159..1187,1200..5079',\
                '8360..8395,9912..10043'],\
                ['start=1','start=1','start=2','start=1','start=3','start=1'],
                ['22..7953','103,6012','21..1234',\
                '32..13123','55..6023','8099..11034']]
            
        db_input_result.append(db_result)
        db_result = db_input_result 
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

print("Database request results:",db_result)

'''
--------------------------------------------------------------------------------
---------------
 KNOWN ISSUES
---------------

1. Need to convert to automatic rather than manual entry of parameters.

--------------------------------------------------------------------------------

'''
