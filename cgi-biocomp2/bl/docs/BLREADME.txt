Basic API (Needs improvement all brackets are going to be deleted or improved on just for us now)

Function: retrieve_basic
Input: search string (radio selection + submission from the retrieve all button (im not sure of your formatting yet))
Output: output from the search using the data type number 5? from the browse functionality supplied by georgina

Function: coding_regions
Input: search string (what they type + radio selection)
Output: string dna with <indicating the start and > indicating the end characters outlining the coding regions

Function: coding_seq
Input: search string (what they type + radio selection)
Output: string of combined coding sequence (can add a symbol between "splice" areas if wanted)

Function: protein_seq
Input: search string (what they type + radio selection)
Output: string of 3 letter amino acids which aligns to the coding seq above (can combine these if we want)

Function: codon_freq_gene
Input: search string (what they type + radio selection)
Output: dictionary with in the format (codon:frequency) will add a codon titled cou (short for count) with the total codons. (I could also make a % caculator but need to decide if I do it or front end)

Function: retrieve_all
Input: search string (radio selection + submission from the retrieve all button (im not sure of your formatting yet))
Output: string of all the data provided by the search using data type number 6-9 from the browse function

Function: show_known_re
Input: search string (this is not to be stored in the database so just call this function when they click a buttion like "supported RE's")
Output: string of all the RE's able to be checked by the middle tier

Function: any_coding_re
Input: search string (what they type + radio selection)
Output: dictionary with the format (restriction enzyme:binding sites) (this one im not sure on a good output but this seemed sensible as there might be multiple enzymes binding) this will only return information if there is
binding in the coding region.

This is subject to change but the general idea such as the function names and general input outputs will stay the same unless we all decide a better format is appropiate. Let me know if you think I forgot anything or want clarity
all of these will search the database as discussed and handle information in some way 