Business Layer API

Function: retrieve_basic
Input: search string (user input + radio selection)
Output: output from the search using the data type number 7 from the base layer: accession, protein name, gene name 
and gene location

Function: coding_regions
Input: search string (user input + radio selection)
Output: string dna with <indicating the start and > indicating the end characters outlining the coding regions

Function: coding_seq
Input: search string (user input + radio selection)
Output: string of combined coding sequence 

Function: protein_seq
Input: search string (user input + radio selection)
Output: string of 3 letter amino acids which aligns to the coding seq above (can combine these if we want)

Function: codon_freq_gene
Input: search string (user input + radio selection)
Output: dictionary with in the format (codon:frequency) will add a codon titled total with the total codons. 

Function: retrieve_all
Input: none calling the function will return everything
Output: string of all the basic data stored in the database: accession, protein name, gene name and gene location

Function: show_known_re
Input: none calling the function returns the information
Output: string of all the RE's able to be checked by the middle tier

Function: any_coding_re
Input: search string (user input + radio selection)
Output: string of dna with  <indicating the start and > indicating the end characters outlining the coding regions.
Restriction enzyme binding sites are highlighted in the same string diffrently depending on the enzyme as seen below.
Echo R1: Start: £ End: $
BamH1: Start: % End: ^
MLuL: Start: & End: *
BsuM1: Start: ( End: )
