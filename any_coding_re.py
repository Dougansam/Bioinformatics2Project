import re

def search(result):
    if result is "1A":
        result = ["cacccacatataacccaatgtatttatatatccaggacctcatattttgcctattgaattctaataataataaacgcgtaacctttgtcgtgtcgatcacttacctacccaggactcacaccaggactcatacacttacacccacatataacccaatgtatttatatatccaggactcatattttgcctattaattctaataataataaagaacctttgtcgtgtcgatcacttacctacccaggactcacaccaggaattcctcatacacttaa"],["90..100,110..113,.132..140"],["start=3"],["AY177663"]
        return result
    else:
        print("fail")
        
def any_coding_re(query):
    aa = []
    code= search(query)
    seq = "".join(code[0])
    introns = "".join(code[1])
    start = "".join(code[2])
    juststartingframe = start[6]
    if juststartingframe is "1":
        startseq = seq
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
    match_echor1 = re.compile("gaattc")
    count = 0
    for r in match_echor1.finditer(finalseq):
        potential = r.span()
        potential_start = int(potential[0])
        potential_start_two = int(potential[0])
        finalseq = "".join(finalseq[:potential_start] + "*" + finalseq[potential_start_two:])
    match_ava11 = re.compile("gg(a|t)cc")
    count = 0
    for r in match_ava11.finditer(finalseq):
        potential = r.span()
        potential_start = int(potential[0])
        potential_start_two = int(potential[0])
        finalseq = "".join(finalseq[:potential_start] + "^" + finalseq[potential_start_two:])
    match_mlul = re.compile("acgcgt")
    count = 0
    for r in match_mlul.finditer(finalseq):
        potential = r.span()
        potential_start = int(potential[0])
        potential_start_two = int(potential[0])
        finalseq = "".join(finalseq[:potential_start] + "&" + finalseq[potential_start_two:])
    return(finalseq)

typed = "1A"
coding_re= any_coding_re(typed)
print(coding_re)
