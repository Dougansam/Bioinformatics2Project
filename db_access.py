
def db_request(db_input, db_query, db_output):

    """Returns specified DB records following a request from BL"""
    
    db_result = []
    db_input_result = []
    
    # Unique string search terms
    
    if db_query != "B" and db_input == 1:
        
        if db_output == 1: 
            #  data_acc_code
            db_result = [["AF485254"],["AF485254"]]
        elif db_output == 2:
            #  data_chrom_loc
            db_result = [["18q24.3"],["U55184"]]
        elif db_output == 3:
            #  data_gene_id
            db_result = [["NPC1"],["U11424"]]
        elif db_output == 4:
            #  data_prot_name
            db_result = [["desmoglein type 1"],["AJ001716"]]
        elif db_output == 5:
            #  data_gene_seq
            db_result = [["gtaagtatcttagcgtcattttctactatgacctgagggttgctac"],\
                           ["U19568"]]
        elif db_output == 6:
            #   data_exon_map
            db_result = [["179..5187,6619..7050"],["D00596"]]
        elif db_output == 7:
            #   data_list_short
            db_result = [["D00596"],["18q24"],["TPMT"],["desmoglein type 1"]]
        elif db_output == 8:
            #   data_list_long
            db_result = [["U11424"],["18q11.2"],["DSG1"],\
            ["desmoglein type 1"],["cacccacatatgtcgtgtcgatcacccaccac"],\
            ["99..987,6619..7050", "20..125, 300..490"]]

        return db_result

    # Non-unique string search terms

    if db_query != "B":
        if db_input == 2 or db_input == 3 or db_input == 4:
                
            if db_output == 1: 
                #  data_acc_code
                db_result = [["AF485254"],["AF485254"]]
            elif db_output == 2:
                #  data_chrom_loc
                db_result = [["18q24.3","18q24"],["AF485254","U49845"]]
            elif db_output == 3:
                #  data_gene_id
                db_result = [["NPC1","NPC1R","pseudoNPC1a"],\
                          ["AF485254","U49845","AF165912"]]
            elif db_output == 4:
                #  data_prot_name
                db_result = [["desmoglein type 1","desmoglein 4 preproprotein"],\
                          ["AF485254","U49845"]]
            elif db_output == 5:
                #  data_gene_seq
                db_result = [["gtaagtatcttagcgtcattttctactatgacctgagggttgctac"],\
                           ["AF485254"]]
            elif db_output == 6:
                #   data_exon_map
                db_result = [["179..5187,6619..7050"],\
                           ["AF485254"]]
            elif db_output == 7:
                #   data_list_short
                db_result = [["D00596","U11424"],\
               ["18q24","18q24"],["TPMT","pseudoTPMT"],\
                ["desmoglein type 1","desmoglein 4 preproprotein"]]
            elif db_output == 8:
                #   data_list_long
                db_result = [["D00596","U11424"],["18q24","18q24"],
                ["TPMT", "pseudoTPMT"],\
                ["desmoglein type 1","desmoglein 4 preproprotein"],     
                ["cacccacatataacccaatgtatttataatttgtcgtgtcgatcacccaccac",\
                "tcttagaaggtatcttagcgtcattttctactacctatatataacaatgacaac"],\
               ["99..987,6619..7050", "20..125, 300..490"]]
 
            return db_result
    
    # Browse input categories
     
    if db_query == "B":
        if db_input != db_output:
        
            if db_input == 1:
                #   list_acc_code
                db_input_result = [[["AF485251","U49845","AF165912","AJ001716",\
                "U19576", "U55184"],["AF485251","U49845","AF165912",\
                "AJ001716","U19576","U55184"]]]
            elif db_input == 2:
                #   list_chrom_loc
                db_input_result = [[["18q24.3","18q24","18q24","18q11.2","q12.1",\
                "18q11"],["AF485254","U49845","AF165912","U55184",\
                "U19576", "U55184"]]]
            elif db_input == 3:
                #   list_gene_id
                db_input_result = [[["NPC1","TPMT","pseudoTPMT","DSG1","DSG1",\
                "SALL3"],["AF485254","U49845","AF165912","AJ001716",\
                "U19576","U55184"]]]
            elif db_input == 4:
                #   list_prot_name
                db_input_result  = [[["Niemann-Pick C1 disease protein",\
                "Niemann-Pick C1 disease protein receptor","desmoglein type 1",\
                "desmoglein 4 preproprotein",\
                "spalt-like zinc finger protein","ferrochelatase"],\
                ["AF485254","U49845","AF165912",\
                "AJ001716","U19576","U55184"]]]
            elif db_input == 5:
                #   list_gene_seq
                db_input_result = [[["cacccacatataacccaatgtatttataatgacctactcatattctcacacc",\
                "tcttagaaggtatcttagcgtcattttctactacctatatataacatgaccttgggtttgactaaac",\
                "aggactcatacactacacatacacatataacatattatataacatcttttattaacatgtatttctt",\
                "tatatccaggatcatattttgcctgaacctttgtcgatcacttacctaatattaaactgatgccat"],\
                ["AF485254","U49845","AF165912","AJ001716"]]]
            elif db_input == 6:
                #   list_exon_map
                db_input_result = [[["1799..5187,6619..7050","20..125, 300..490",\
                "99..587,619..1150","111..183,8360..8395,9912..10043,11591..11746",\
                "159..1187,1200..5079","8360..8395,9912..10043"],\
                ["AF485254","U49845","AF165912","AJ001716","U19576","U55184"]]]
            elif db_input  == 7:      
                #   list_short
                db_input_result = [[["D00596","U11424","U19568","U19576"],\
                ["18q24.3","18q24","18q24","18q11.2"],\
                ["NPC1","TPMT","pseudoTPMT","DSG1"],\
                ["desmoglein type 1","desmoglein 4 preproprotein",\
                "spalt-like zinc finger protein","ferrochelatase"]]]
            elif db_input == 8:
                #   list_long
                db_input_result = [[["D00596","U11424","U19568","U19576"],\
                ["18q24.3","18q24","18q24","18q11.2"],\
                ["NPC1","TPMT","pseudoTPMT","DSG1"],\
                ["desmoglein type 1","desmoglein 4 preproprotein",\
                "spalt-like zinc finger protein","ferrochelatase"],             
                ["cacccacatataaataataataaagaacctttgtcgtgtcgatcacccaccagctcacacc",\
                "tcttagaaggtatcttagcgtcattttctactacctatatataacaatgacctgggtttgactaaac",\
                "aggactcatacactacacatacacatataacatattatataacatcttaccttaacatgtatttctt",\
                "tatatccaggatcatattttgcctgaacctttgtcgatcacttacctaaccttaaactgatgccat"],\
                ["99..987,6619..7050", "20..125, 300..490","99..587,619..950",\
                "11..183,8360..8395,9912..10043,11591..11751"]]]    

        # Browse additional output categories

        if db_output == 1:
            #   list_acc_code
            db_result = [["AF485250","U49845","AF165912","AJ001716",\
            "U19576", "U55184"],["AF485250","U49845","AF165912",\
            "AJ001716","U19576","U55184"]]
        elif db_output == 2:
             #   list_chrom_loc
            db_result = [["18q24.3","18q24","18q24","18q11.2","q12.1",\
            "18q11"],["AF485254","U49845","AF165912","U55184",\
            "U19576", "U55184"]]
        elif db_output == 3:
            #   list_gene_id
            db_result = [["NPC1","TPMT","pseudoTPMT","DSG1","DSG1",\
            "SALL3"],["AF485254","U49845","AF165912","AJ001716",\
            "U19576","U55184"]]
        elif db_output == 4:
            #   list_prot_name
            db_result = [["Niemann-Pick C1 disease protein",\
            "Niemann-Pick C1 disease protein receptor","desmoglein type 1",\
            "desmoglein 4 preproprotein",\
            "spalt-like zinc finger protein","ferrochelatase"],\
            ["AF485254","U49845","AF165912",\
            "AJ001716","U19576","U55184"]]
        elif db_output == 5:
            #   list_gene_seq
            db_result = [["cacccacatataacccaatgtatttataatgacctactcatattctcacacc",\
            "tcttagaaggtatcttagcgtcattttctactacctatatataacatgaccttgggtttgactaaac",\
            "aggactcatacactacacatacacatataacatattatataacatcttttattaacatgtatttctt",\
            "tatatccaggatcatattttgcctgaacctttgtcgatcacttacctaatattaaactgatgccat"],\
            ["AF485254","U49845","AF165912","AJ001716"]]
        elif db_output == 6:
            #   list_exon_map
            db_result = [["1799..5187,6619..7050","20..125, 300..490",\
            "99..587,619..1150","111..183,8360..8395,9912..10043,11591..11746",\
            "159..1187,1200..5079","8360..8395,9912..10043"],\
            ["AF485254","U49845","AF165912","AJ001716","U19576","U55184"]]
        elif db_output  == 7:      
            #   list_short
            db_result = [["D00596","U11424","U19568","U19576"],\
            ["18q24.3","18q24","18q24","18q11.2"],\
            ["NPC1","TPMT","pseudoTPMT","DSG1"],\
            ["desmoglein type 1","desmoglein 4 preproprotein",\
            "spalt-like zinc finger protein","ferrochelatase"]]
        elif db_output == 8:
            #   list_long
            db_result = [["D00596","U11424","U19568","U19576"],\
            ["18q24.3","18q24","18q24","18q11.2"],\
            ["NPC1","TPMT","pseudoTPMT","DSG1"],\
            ["desmoglein type 1","desmoglein 4 preproprotein",\
            "spalt-like zinc finger protein","ferrochelatase"],             
            ["cacccacatataaataataataaagaacctttgtcgtgtcgatcacccaccagctcacacc",\
            "tcttagaaggtatcttagcgtcattttctactacctatatataacaatgacctgggtttgactaaac",\
            "aggactcatacactacacatacacatataacatattatataacatcttaccttaacatgtatttctt",\
            "tatatccaggatcatattttgcctgaacctttgtcgatcacttacctaaccttaaactgatgccat"],\
            ["99..987,6619..7050", "20..125, 300..490","99..587,619..950",\
            "11..183,8360..8395,9912..10043,11591..11750"]]
            
        db_input_result.append(db_result)
        db_result = db_input_result
        
    return db_result



  
