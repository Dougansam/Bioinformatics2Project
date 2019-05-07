import sys
sys.path.insert(0, "../bl")
import blapi

#test feature tests output of dummy data if the program is run directly.
#uses dummy data to test if the functions call the base layer correctly.

if __name__ == "__main__":
    radio = "accession"
    typed = "test"
    print (any_coding_re(radio ,typed))
    print (coding_regions(radio, typed))
    print (coding_seq(radio, typed))
    print (codon_freq_gene(radio, typed))
    print (protein_seq(radio, typed))
    print (retrieve_all())
    print (retrieve_basic(radio, typed))
    print (show_known_re())
