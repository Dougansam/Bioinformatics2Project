
def search(result):
    if result is "1A":
        result = ["cacccacatataacccaatgtatttatatatccaggactcatattttgcctattaattctaataataataaagaacctttgtcgtgtcgatcacttacctacccaggactcacaccaggactcatacacttacacccacatataacccaatgtatttatatatccaggactcatattttgcctattaattctaataataataaagaacctttgtcgtgtcgatcacttacctacccaggactcacaccaggactcatacactta"],["90..100,110..113,.132..140"],["start=3"],["AY177663"]
        return result
    else:
        print("fail")

def codon_freq_gene(query):
    codon_freq = {'cou':0}
    code= search(query)
    seq = "".join(code[0])
    introns = "".join(code[1])
    start = "".join(code[2])
    #intronlocations = re.findall(r'\d+', introns)
    #finalseq = []
    #for i in range(0, len(intronlocations), 2):
        #intronsliceone = int(intronlocations[i])
       # intronslicetwo = int(intronlocations[i+1])
        #finalseq.append(seq[intronsliceone:intronslicetwo])
    #finalseq = "".join(finalseq)
    codons =(seq[i:i+3] for i in range(0, len(seq), 3))
    for codon in codons:
        if codon in codon_freq:
            codon_freq[codon] += 1
            codon_freq['cou'] += 1
        else:
            codon_freq[codon] = 1
            codon_freq['cou'] += 1
    return codon_freq

typed = "1A"
codonfreq= codon_freq_gene(typed)
print(codonfreq)

