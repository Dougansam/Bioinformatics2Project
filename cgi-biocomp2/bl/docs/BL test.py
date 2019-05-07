import re
import sys
sys.path.insert(0, "../")
import blapi

#test feature tests output of dummy data if the program is run directly.
#uses dummy data to test if the functions call the base layer correctly.

if __name__ == "__main__":
    radio = "accession"
    typed = "test"
    print (blapi.any_coding_re(radio ,typed))
    print (blapi.coding_regions(radio, typed))
    print (blapi.coding_seq(radio, typed))
    print (blapi.codon_freq_gene(radio, typed))
    print (blapi.protein_seq(radio, typed))
    print (blapi.retrieve_all())
    print (blapi.retrieve_basic(radio, typed))
    print (blapi.show_known_re())
    print (blapi.whole_chrom_codons())

    
#written by Sam Dougan
