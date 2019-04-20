'''
123456789012345678901234567890123456789012345678901234567890123456789012------9
'''

def db_request(db_input, db_query, db_output):

    """Returns specified DB records following a request from BL"""
    
    db_result = []
    db_input_result = []
    
    # Unique string search terms
    
    if db_query != 'B' or 'b' and db_input == 1:
        
        if db_output == 1: 
            #  data_acc_code
            db_result = [['AF485254'],['AF485254']]
        elif db_output == 2:
            #  data_chrom_loc
            db_result = [['18q24.3'],['U55184']]
        elif db_output == 3:
            #  data_gene_id
            db_result = [['NPC1'],['U11424']]
        elif db_output == 4:
            #  data_prot_name
            db_result = [['desmoglein type 1'],['AJ001716']]
        elif db_output == 5:
            #  data_gene_seq
            db_result = [['gtaagtatcttagcgtcattttctactatgacctgagggttgctac'],\
                        ['U19568']]
        elif db_output == 6:
            #   data_exon_map
            db_result = [['179..5187,6619..7050'],['start=1'],['D00596']]
        elif db_output == 7:
            #   data_list_short
            db_result = [['D00596'],['18q24'],['TPMT'],['desmoglein type 1']]
        elif db_output == 8:
            #   data_list_long
            db_result = [['U11424'],['18q11.2'],['DSG1'],\
                        ['desmoglein type 1'],\
                        ['caccttctactatgacctgagggttgctacatcacccaccac'],\
                        ['3..18','20..25'],['start=3']]

        return db_result

    # Non-unique string search terms

    if db_query != 'B' or 'b':
        if db_input == 2 or db_input == 3 or db_input == 4:
                
            if db_output == 1: 
                #  data_acc_codes
                db_result = [['AF485254'],['AF485254'],\
                            ['AF485254'],['AF485254']]
            elif db_output == 2:
                #  data_chrom_locs
                db_result = [['18q24.3','18q24'],['AF485254','U49845']]
            elif db_output == 3:
                #  data_gene_ids
                db_result = [['NPC1','NPC1R','pseudoNPC1a'],\
                            ['AF485254','U49845','AF165912']]
            elif db_output == 4:
                #  data_prot_names
                db_result = \
                [['desmoglein type 1','desmoglein 4 preproprotein'],\
                ['AF485254','U49845']]
            elif db_output == 5:
                #  data_gene_seqs
                db_result = \
                [['gtaagtatcttagcgtcattttctactatgacctgagggttgctac'],\
                ['AF485254']]
            elif db_output == 6:
                #   data_exon_maps
                db_result = [['179..5187,6619..7050'],\
                ['start=2'],['AF485254']]
            elif db_output == 7:
                #   data_lists_short
                db_result = [['D00596','U11424'],\
                ['18q24','18q24'],['TPMT','pseudoTPMT'],\
                ['desmoglein type 1','desmoglein 4 preproprotein']]
            elif db_output == 8:
                #   data_lists_long
                db_result = [['D00596','U11424'],['18q24','18q24'],
                ['TPMT','pseudoTPMT'],\
                ['desmoglein type 1','desmoglein 4 preproprotein'],\
                ['cacccacatataacccaatgtatttataatttgtcgtgtcgatcacccaccac',\
                'tcttagaaggtatcttagcgtcattttctactacctatatataacaatgacaac'],\
                ['99..987,6619..7050','20..125,300..490'],\
                ['start=1','start=3']]
   
            return db_result
    
    # Browse input categories
     
    if db_query == 'B' or 'b':
        if db_input != db_output:
        
            if db_input == 1:
                #   list_acc_codes
                db_input_result = [[['AF485251','U49845','U19576', 'U55184',\
                'AF165912','AJ001716'],['AF485251','U49845','U19576', 'U55184',\
                'AF165912','AJ001716']]]
            elif db_input == 2:
                #   list_chrom_locs
                db_input_result = [[['18q24.3','18q24','18q24','18q11.2',\
                'q12.1','18q11'],['AF485251','U49845','U19576', 'U55184',\
                'AF165912','AJ001716']]]
            elif db_input == 3:
                #   list_gene_ids
                db_input_result = [[['NPC1','TPMT','pseudoTPMT','DSG1',\
                'DSG1','SALL3'],['AF485251','U49845','U19576', 'U55184',\
                'AF165912','AJ001716']]]
            elif db_input == 4:
                #   list_prot_names
                db_input_result = [[['Niemann-Pick C1 disease protein',\
                'Niemann-Pick C1 disease protein receptor',\
                'desmoglein type 1','desmoglein 4 preproprotein',\
                'spalt-like zinc finger protein','ferrochelatase'],\
                ['AF485251','U49845','U19576','U55184','AF165912','AJ001716']]]
            elif db_input == 5:
                #   list_gene_seqs
                db_input_result = [[['cacccacataacatataacatattcgtaacctcacacc',\
                'tcttagaaggtatcttagcgtcattttctactacctatatataatgggtttgactaaac',\
                'aggactcatacactacacatacacatataacatatttcttttattaacatgtatttctt',\
                'ggttagaaggtatcttagcgtcattttcatatataacatgaccttgggtttgactaaac',\
                'ctgactcatacaccacatataacatattatataacatcttttattaacatgtatttctt',\
                'tatatccaggatatattttgctttgtcgatcacttacctaatattaaactgatgccat'],\
                ['AF485251','U49845','U19576','U55184','AF165912','AJ001716']]]
            elif db_input == 6:
                #   list_exon_maps
                db_input_result = [[['179..5187,6619..7050','NF',\
                '99..587,619..1150','111..183,8360..8395, 11591..11746',\
                '159..1187,1200..5079','8360..8395,9912..10043'],
                ['start=1','start=1','start=2','start=1','start=3','start=1'],\
                ['AF485251','U49845','U19576','U55184','AF165912','AJ001716']]]
            elif db_input == 7:      
                #   data_lists_short
                db_input_result = [[['AF485251','U49845','U19576','U55184',\
                'AF165912','AJ001716'],['18q24.3','18q24','18q24','18q11.2',\
                'q12.1','18q11'],['NPC1','TPMT','pseudoTPMT','DSG1','DSG1',\
                'SALL3'],['Niemann-Pick C1 disease protein',\
                'Niemann-Pick C1 disease protein receptor','desmoglein type 1',\
                'desmoglein 4 preproprotein','spalt-like zinc finger protein',\
                'ferrochelatase']]]
            elif db_input == 8:
                #   data_lists_long
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
                'start=1','start=3','start=1']]]  

        # Browse additional output categories

        if db_output == 1:
            #   list_acc_codes
            db_result = [['AF485251','U49845','U19576','U55184','AF165912',\
            'AJ001716'],['AF485251','U49845','U19576', 'U55184','AF165912',\
            'AJ001716']]    
        elif db_output == 2:
             #   list_chrom_locs
            db_result = [['18q24.3','18q24','18q24','18q11.2',\
                'q12.1','18q11'],['AF485251','U49845','U19576', 'U55184',\
                'AF165912','AJ001716']]
        elif db_output == 3:
            #   list_gene_ids
            db_result = [['NPC1','TPMT','pseudoTPMT','DSG1',\
                'DSG1','SALL3'],['AF485251','U49845','U19576', 'U55184',\
                'AF165912','AJ001716']]
        elif db_output == 4:
            #   list_prot_names
            db_result = [['Niemann-Pick C1 disease protein',\
                'Niemann-Pick C1 disease protein receptor',\
                'desmoglein type 1','desmoglein 4 preproprotein',\
                'spalt-like zinc finger protein','ferrochelatase'],\
                ['AF485251','U49845','U19576','U55184','AF165912','AJ001716']]
        elif db_output == 5:
            #   list_gene_seqs
            db_result = [['cacccacataacatataacatattcgtaacctcacacc',\
                'tcttagaaggtatcttagcgtcattttctactacctatatataatgggtttgactaaac',\
                'aggactcatacactacacatacacatataacatatttcttttattaacatgtatttctt',\
                'ggttagaaggtatcttagcgtcattttcatatataacatgaccttgggtttgactaaac',\
                'ctgactcatacaccacatataacatattatataacatcttttattaacatgtatttctt',\
                'tatatccaggatatattttgctttgtcgatcacttacctaatattaaactgatgccat'],\
                ['AF485251','U49845','U19576','U55184','AF165912','AJ001716']]
        elif db_output == 6:
            #   list_exon_maps
            db_result = [['179..5187,6619..7050','NF',\
                '99..587,619..1150','111..183,8360..8395, 11591..11746',\
                '159..1187,1200..5079','8360..8395,9912..10043'],
                ['start=1','start=1','start=2','start=1','start=3','start=1'],\
                ['AF485251','U49845','U19576','U55184','AF165912','AJ001716']]
        elif db_output  == 7:      
            #   data_lists_short
            db_result = [['AF485251','U49845','U19576','U55184',\
                'AF165912','AJ001716'],['18q24.3','18q24','18q24','18q11.2',\
                'q12.1','18q11'],['NPC1','TPMT','pseudoTPMT','DSG1','DSG1',\
                'SALL3'],['Niemann-Pick C1 disease protein',\
                'Niemann-Pick C1 disease protein receptor','desmoglein type 1',\
                'desmoglein 4 preproprotein','spalt-like zinc finger protein',\
                'ferrochelatase']]
        elif db_output == 8:
            #   data_lists_long
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
                '8360..8395,9912..10043'],['start=1','start=1','start=2',\
                'start=1','start=3','start=1']]
            
        db_input_result.append(db_result)
        db_result = db_input_result
        
    return db_result



  
