import re
import sys
sys.path.insert(0, "../db/")
import dbapi

#All written by Sam Dougan
#*******************************************************************************
         
def any_coding_re(radio, query):

    '''
    restriction enzyme biding site function. Takes in query and radio from
    front end and searches database for results. handles the data returned
    and produces a string of dna. Coding regions marked by <> characters.
    EchoR1 binding sites outlined by £$. BamH1 marked by %^, Mlul marked by
    &* and finally BsuM1 marked by ().
    '''
    
    aa = []
    #the radios are converted to the int value reconised by the database
    if radio == "accession":
        radio = 1
    if radio == "chr_location":
        radio = 2
    if radio == "gene_id":
        radio = 3
    if radio == "gene_product":
        radio = 4
        
    #this value is used in the databse to identify the data needed
    wanted = 8
    code= db_request(radio, query, wanted)
    seq = "".join(code[4])
    introns = "".join(code[5])
    start = "".join(code[6])
    juststartingframe = start[6]

    #deleting entrys from the start to align reading frame in these senarios
    #these values will not ever be read
    if juststartingframe is "1":
        startseq = seq
    if juststartingframe is "2":
        startseq = seq[1:]
    if juststartingframe is "3":
        startseq = seq[2:]
        
    #regexing out just the numbers from the introns section to allow for
    #splicing
    intronlocations = re.findall(r'\d+', introns)
    finalseq = []
    
    #Moving through the numbers stored in intronlocations as twos
    #the first is used to insert the opening < symbol then the second
    #is inserted to close > the coding region. the second is then stored as
    #the start location for the next slice to move through the code.
    #finally the remaining code after the last slice is added to complete the
    #sequence and is joined into a string.
    lastslice = 0
    for i in range(0, len(intronlocations), 2):
        intronsliceone = int(intronlocations[i])
        intronslicetwo = int(intronlocations[i+1])
        finalseq.append(startseq[lastslice:intronsliceone] + "<")
        finalseq.append(startseq[intronsliceone:intronslicetwo] + ">")
        lastslice = intronslicetwo
    finalseq.append(startseq[intronslicetwo:])
    finalseq = "".join(finalseq)
    
    #if the first base was removed the first base is readded to the sequence
    if juststartingframe is "2":
        finalseq = "".join(seq[:1] + finalseq)
    if juststartingframe is "3":
        finalseq = "".join(seq[:2] + finalseq)
        
    #for each selected restriction enzyme regex is used to identify the pattern
    #if a match is found in the sequence then the span of the match is stored
    #this span is used to cut out the match and replaced in the string with
    #markers added. due to the chosen enzymes having no variable bases the final
    #sequence is joined and returned to the front end.
    match_echor1 = re.compile("gaattc")
    for r in match_echor1.finditer(finalseq):
        potential = r.span()
        potential_start = int(potential[0])
        potential_finish = int(potential[1])
        finalseq = "".join(finalseq[:potential_start] + "£gaattc$" + finalseq[potential_finish:])
    match_bamh1 = re.compile("ggatcc")
    for r in match_bamh1.finditer(finalseq):
        potential = r.span()
        potential_start = int(potential[0])
        potential_start_two = int(potential[0])
        finalseq = "".join(finalseq[:potential_start] + "%ggatcc^" + finalseq[potential_start_two:])
    match_mlul = re.compile("acgcgt")
    for r in match_mlul.finditer(finalseq):
        potential = r.span()
        potential_start = int(potential[0])
        potential_finish = int(potential[1])
        finalseq = "".join(finalseq[:potential_start] + "&acgcgt*" + finalseq[potential_finish:])
    match_bsum1 = re.compile("ctcgag")
    for r in match_bsum1.finditer(finalseq):
        potential = r.span()
        potential_start = int(potential[0])
        potential_start_two = int(potential[0])
        finalseq = "".join(finalseq[:potential_start] + "(ctcgag)" + finalseq[potential_start_two:])
    return(finalseq)

#*******************************************************************************

def coding_regions(radio ,query):

    '''
    Coding region highlighter. This function takes in a query and the radio
    information from the front end and sends this to the database layer.
    the output is seperated and used to highlight areas of coding regions
    in the DNA stored in the database. This is highlighted using <> symbols
    around the coding regions to be highlighed in the HTML
    '''
    
    coding = []
    #the radios are converted to the int value reconised by the database
    if radio == "accession":
        radio = 1
    if radio == "chr_location":
        radio = 2
    if radio == "gene_id":
        radio = 3
    if radio == "gene_product":
        radio = 4
        
    #this value is used in the databse to identify the data needed
    wanted = 8
    code= db_request(radio ,query, wanted)
    
    #the information comes back in a list below seperates this list into
    #varables that are easy to use
    seq = "".join(code[4])
    introns = "".join(code[5])
    start = "".join(code[6])
    juststartingframe = start[6]
    
    #deleting entrys from the start to align reading frame in these senarios
    #these values will not ever be read
    if juststartingframe is "2":
        startseq = seq[1:]
    if juststartingframe is "3":
        startseq = seq[2:]
        
    #regexing out just the numbers from the introns section to allow for
    #splicing
    intronlocations = re.findall(r'\d+', introns)
    finalseq = []
    
    lastslice = 0
    #Moving through the numbers stored in intronlocations as twos
    #the first is used to insert the opening < symbol then the second
    #is inserted to close > the coding region. the second is then stored as
    #the start location for the next slice to move through the code.
    #finally the remaining code after the last slice is added to complete the
    #sequence and is joined into a string.
    for i in range(0, len(intronlocations), 2):
        intronsliceone = int(intronlocations[i])
        intronslicetwo = int(intronlocations[i+1])
        finalseq.append(startseq[lastslice:intronsliceone] + "<")
        finalseq.append(startseq[intronsliceone:intronslicetwo] + ">")
        lastslice = intronslicetwo
    finalseq.append(startseq[intronslicetwo:])
    finalseq = "".join(finalseq)
    #if the first base was removed the first base is readded to the sequence
    
    if juststartingframe is "2":
        finalseq = "".join(seq[:1] + finalseq)
    if juststartingframe is "3":
        finalseq = "".join(seq[:2] + finalseq)
    return finalseq

#*******************************************************************************

def coding_seq(radio, query):

    '''
    This function splices out the coding sequence rather than just highlighting.
    this sequence will align with the protein coding sequence. The function takes
    A radio and a query to be passed to the database which returns information
    needed to locate the coding sequence. The output is a string of DNA code
    that will code for the protein.
    '''
    
    coding = []
    #the radios are converted to the int value reconised by the database
    if radio == "accession":
        radio = 1
    if radio == "chr_location":
        radio = 2
    if radio == "gene_id":
        radio = 3
    if radio == "gene_product":
        radio = 4
        
    #this value is used in the databse to identify the data needed
    wanted = 8
    code= db_request(radio, query, wanted)
    
    #the information comes back in a list below seperates this list into
    #varables that are easy to use
    seq = "".join(code[4])
    introns = "".join(code[5])
    start = "".join(code[6])
    juststartingframe = start[6]
    
    #deleting entrys from the start to align reading frame in these senarios
    #these values will not ever be read
    if juststartingframe is "2":
        seq = seq[1:]
    if juststartingframe is "3":
        seq = seq[2:]
        
    #regexing out just the numbers from the introns section to allow for
    #splicing
    intronlocations = re.findall(r'\d+', introns)
    #splicing of the sequence and saving the splices into finalseq
    finalseq = []
    for i in range(0, len(intronlocations), 2):
        intronsliceone = int(intronlocations[i])
        intronslicetwo = int(intronlocations[i+1])
        finalseq.append(seq[intronsliceone:intronslicetwo])
    finalseq = "".join(finalseq)
    return finalseq

#*******************************************************************************

def codon_freq_gene(radio, query):

    '''
    This function is a codon frequency caculator. It takes in information on the
    radio selected and the stringquery from the front end and packages this for
    the database layer. It cuts the code given back into coding sequence and counts
    the codons in the sequence as well as a total. This is stored in a dictionary
    and passed back to the front layer.
    '''
    codon_freq = {'total':0}
    #the radios are converted to the int value reconised by the database
    if radio == "accession":
        radio = 1
    if radio == "chr_location":
        radio = 2
    if radio == "gene_id":
        radio = 3
    if radio == "gene_product":
        radio = 4
    #this value is used in the databse to identify the data needed
    wanted = 8
    code= db_request(radio, query, wanted)
    
    #the information comes back in a list below seperates this list into
    #varables that are easy to use
    seq = "".join(code[4])
    introns = "".join(code[5])
    start = "".join(code[6])
    juststartingframe = start[6]
    
    #deleting entrys from the start to align reading frame in these senarios
    #these values will not ever be read
    if juststartingframe is "2":
        seq = seq[1:]
    if juststartingframe is "3":
        seq = seq[2:]
        
    #regexing out just the numbers from the introns section to allow for
    #splicing
    intronlocations = re.findall(r'\d+', introns)
    #splicing of the sequence and saving the splices into finalseq
    finalseq = []
    for i in range(0, len(intronlocations), 2):
        intronsliceone = int(intronlocations[i])
        intronslicetwo = int(intronlocations[i+1])
        finalseq.append(seq[intronsliceone:intronslicetwo])
    finalseq = "".join(finalseq)
    
    #joining finalseq to a string and going through the string in threes
    #if the codons are unique they are added as a new key in the
    #dictionary if not 1 is added to the value. In both cases 1 is added
    #to the total so a percentage can be caculated on the front end.
    codons =(finalseq[i:i+3] for i in range(0, len(finalseq), 3))
    for codon in codons:
        if codon in codon_freq:
            codon_freq[codon] += 1
            codon_freq['total'] += 1
        else:
            codon_freq[codon] = 1
            codon_freq['total'] += 1
    return codon_freq

#*******************************************************************************

def protein_seq(radio, query):

    '''
    main translating def takes in a search string and outputs the produced protein
    code from the DNA found in the search "query" is the users input. radio is the
    type of data used to search such as assession code to be passed down to the db
    the output is single amino acid codes with X being a stop codon.
    '''
    
    aa = []
    #the radios are converted to the int value reconised by the database
    if radio == "accession":
        radio = 1
    if radio == "chr_location":
        radio = 2
    if radio == "gene_id":
        radio = 3
    if radio == "gene_product":
        radio = 4
    #this value is used in the databse to identify the data needed
    wanted = 8
    code= db_request(radio, query, wanted)
    
    #the information comes back in a list below seperates this list into
    #varables that are easy to use
    seq = "".join(code[4])
    introns = "".join(code[5])
    start = "".join(code[7])
    juststartingframe = start[6]
    
    #deleting entrys from the start to align reading frame in these senarios
    #these values will not ever be read
    if juststartingframe is "2":
        seq = seq[1:]
    if juststartingframe is "3":
        seq = seq[2:]
        
    #regexing out just the numbers from the introns section to allow for
    #splicing
    intronlocations = re.findall(r'\d+', introns)
    finalseq = []
    #splicing of the sequence and saving the splices into finalseq
    for i in range(0, len(intronlocations), 2):
        intronsliceone = int(intronlocations[i])
        intronslicetwo = int(intronlocations[i+1])
        finalseq.append(seq[intronsliceone:intronslicetwo])
    finalseq = "".join(finalseq)
    
    #Going through the finalseq in threes and assigning a one letter
    #amino acid code to the codon given. this moves through the whole
    #finalseq variable returning the full set at the end as a string.
    for i in range(0, len(finalseq), 3):
        codon = finalseq[i:i+3]
        if codon in ("att", "atc", "ata"):
           aa.append(" I ")
        if codon in ("ctt", "ctc", "cta", "ctg", "tta", "ttg"):
           aa.append(" L ")
        if codon in ("gtt", "gtc", "gta", "gtg"):
           aa.append(" V ")
        if codon in ("ttt", "ttc"):
           aa.append(" F ")
        if codon in ("atg"):
           aa.append(" M ")
        if codon in ("tgt", "tgc"):
           aa.append(" C ")
        if codon in ("gct", "gcc", "gca", "gcg"):
           aa.append(" A ")
        if codon in ("ggt", "ggc", "gga", "ggg"):
           aa.append(" G ")
        if codon in ("cct", "ccc", "cca", "ccg"):
           aa.append(" P ")
        if codon in ("act", "acc", "aca", "acg"):
           aa.append(" T ")
        if codon in ("tct", "tcc", "tca", "tcg", "agt", "agc"):
           aa.append(" S ")
        if codon in ("tat", "tac"):
           aa.append(" Y ")
        if codon in ("tgg"):
           aa.append(" W ")
        if codon in ("caa", "cag"):
           aa.append(" Q ")
        if codon in ("aat", "aac"):
           aa.append(" N ")
        if codon in ("cat", "cac"):
           aa.append(" H ")
        if codon in ("gaa", "gag"):
           aa.append(" E ")
        if codon in ("gat", "gac"):
           aa.append(" D ")
        if codon in ("aaa", "aag"):
           aa.append(" K ")
        if codon in ("cgt", "cgc", "cga", "cgg", "aga", "agg"):
           aa.append(" R ")
        if codon in ("taa", "tag", "tga"):
           aa.append(" X ")
    return "".join(aa)

#*******************************************************************************

def retrieve_all():

    '''
    this function is called through a button in the HTML. it passes a request
    to the database to return the "basic" information stored on all entrys in
    the database: Accession number, gene identifier, location and product.
    this is then displayed on the webpage.
    '''
    
    #this input uses the browse feature of the base layer to return all
    #stored information
    info = db_request(7, 'B', 7)
    return info

#*******************************************************************************

def retrieve_basic(radio, query):

    '''
    This function takes a radio and string query from the front end. This calls the
    database layer inputting the type of data searched on as well as the search
    it returns the base information on the query and multiple if the search is
    not unique. The basic information is: Accession number, gene identifier,
    location and product. If the search is not unique the front end will ask for
    clarification
    '''
    
    #the radios are converted to the int value reconised by the database
    if radio == "accession":
        radio = 1
    if radio == "chr_location":
        radio = 2
    if radio == "gene_id":
        radio = 3
    if radio == "gene_product":
        radio = 4
    #this value is used in the databse to identify the data needed
    wanted = 7
    result = db_request(radio, query, wanted)
    return result

#*******************************************************************************

def show_known_re():

   '''
   This function returns a simple string showing what restriction enzymes are
   supported by the any_coding_re function.
   '''
   
   re = "The four RE's able to be checked for are EchoR1, BamH1, BsuM1 and Mlul"
   return re

#*******************************************************************************

