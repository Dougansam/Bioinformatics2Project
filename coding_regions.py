import re

def search(result):
    if result is "1A":
        result = ["cacccacatataacccaatgtatttatatatccaggactcatattttgcctattaattctaataataataaagaacctttgtcgtgtcgatcacttacctacccaggactcacaccaggactcatacacttacacccacatataacccaatgtatttatatatccaggactcatattttgcctattaattctaataataataaagaacctttgtcgtgtcgatcacttacctacccaggactcacaccaggactcatacactta"],["90..100,110..113,.132..140"],["start=3"],["AY177663"]
        return result
    else:
        print("fail")

def coding_regions(query):
    coding = []
    code= search(query)
    seq = "".join(code[0])
    introns = "".join(code[1])
    start = "".join(code[2])
    juststartingframe = start[6]
    if juststartingframe is "2":
        startseq = seq[1:]
    if juststartingframe is "3":
        startseq = seq[2:]
    intronlocations = re.findall(r'\d+', introns)
    finalseq = []
    lastslice = 0
    for i in range(0, len(intronlocations), 2):
        intronsliceone = int(intronlocations[i])
        intronslicetwo = int(intronlocations[i+1])
        finalseq.append(startseq[lastslice:intronsliceone] + "<")
        finalseq.append(startseq[intronsliceone:intronslicetwo] + ">")
        lastslice = intronslicetwo
    finalseq.append(startseq[intronslicetwo:])
    finalseq = "".join(finalseq)
    if juststartingframe is "2":
        finalseq = "".join(seq[:1] + finalseq)
    if juststartingframe is "3":
        finalseq = "".join(seq[:2] + finalseq)
    return finalseq
    
typed = "1A"
codingregions= coding_regions(typed)
print(codingregions)
