import re

def search(result):
    if result is "1A":
        result = ["cacccacatataacccaatgtatttatatatccaggactcatattttgcctattaattctaataataataaagaacctttgtcgtgtcgatcacttacctacccaggactcacaccaggactcatacacttacacccacatataacccaatgtatttatatatccaggactcatattttgcctattaattctaataataataaagaacctttgtcgtgtcgatcacttacctacccaggactcacaccaggactcatacactta"],["90..100,110..113,.132..140"],["start=3"],["AY177663"]
        return result
    else:
        print("fail")

def coding_seq(query):
    coding = []
    code= search(query)
    seq = "".join(code[0])
    introns = "".join(code[1])
    start = "".join(code[2])
    juststartingframe = start[6]
    if juststartingframe is "2":
        seq = seq[1:]
    if juststartingframe is "3":
        seq = seq[2:]
    intronlocations = re.findall(r'\d+', introns)
    finalseq = []
    for i in range(0, len(intronlocations), 2):
        intronsliceone = int(intronlocations[i])
        intronslicetwo = int(intronlocations[i+1])
        finalseq.append(seq[intronsliceone:intronslicetwo])
    finalseq = "".join(finalseq)
    return finalseq
    
typed = "1A"
codingseq= coding_seq(typed)
print(codingseq)
