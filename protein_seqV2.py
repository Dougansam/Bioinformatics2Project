import re

#fake search def to introduce dummy data to the main functon.
#during final implementation will add more information according to georginas
#api
def search(result):
    if result is "1A":
        result = ["cacccacatataacccaatgtatttatatatccaggactcatattttgcctattaattctaataataataaagaacctttgtcgtgtcgatcacttacctacccaggactcacaccaggactcatacacttacacccacatataacccaatgtatttatatatccaggactcatattttgcctattaattctaataataataaagaacctttgtcgtgtcgatcacttacctacccaggactcacaccaggactcatacactta"],["90..100,110..113,.132..140"],["start=3"],["AY177663"]
        return result
    else:
        print("fail")
        
#main translating def takes in a search string and outputs the produced protein
#code from the DNA found in the search "query" is the users input. int is the
#type of data used to search such as assession code to be passed down to the db
def protein_seq(query):
    aa = []
    code= search(query)
    #the information comes back in a list below seperates this list into
    #varables that are easy to use
    seq = "".join(code[0])
    introns = "".join(code[1])
    start = "".join(code[2])
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
    return "".join(aa)


typed = "1A"
aminoacids= protein_seq(typed)
print(aminoacids)


