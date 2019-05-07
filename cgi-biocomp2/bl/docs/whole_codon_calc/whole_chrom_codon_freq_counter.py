import re
#parser to remove the DNA stored in the ORIGIN section of the genebank records

f= open("chrom_CDS_18","r")

text = f.read()
f.close()

matches= re.findall("ORIGIN[actg \d\n]+\/\/", text)

#cleaning the results of the matches so only the DNA code remains
matches= "".join(matches)
matches= matches.replace('\n', '')
matches= matches.replace("'\n'", '')
matches= matches.replace(' ', '')
matches= matches.replace('ORIGIN', '')
matches= matches.replace('/', '')
matches= matches.translate({ord(i): None for i in '0123456789'})

#printing the output to a file and ensuring no new line is printed at the end
with open("DNA.txt", 'w') as g:
    print(matches, file=g, end='')


#codon counter that takes a text file generated above called DNA.txt as the
#input and outputs a dictionary containing the number of times each codon
#appears in the whole genome.

f= open("DNA.txt","r")
seq = f.read()
f.close()


codon_freq = {'total':0}
codons =(seq[i:i+3] for i in range(0, len(seq), 3))
for codon in codons:
    if codon in codon_freq:
        codon_freq[codon] += 1
        codon_freq['total'] += 1
    else:
        codon_freq[codon] = 1
        codon_freq['total'] += 1
print(codon_freq)
