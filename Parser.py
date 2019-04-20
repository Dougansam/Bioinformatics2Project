import re

with open('genbank2.txt','rt') as myfile:
    for line in myfile:   
        acc_flag = re.compile('(ACCESSION)([\s]+)(([A-Z]+)([0-9]+))')
        acc_found = re.match(acc_flag,line)
        if acc_found != None:
            acc_code = acc_found.group(3)
            print(acc_code,end=',')
print('\n')            
with open('genbank2.txt','rt') as myfile:
    for line in myfile:   
        map_flag = re.compile('([\s]+)(/map=")(.+)(")')
        map_found = re.match(map_flag,line)
        if map_found != None:
            chrom_loc = map_found.group(3)
            print(chrom_loc,end=',')
print('\n')
with open('genbank2.txt','rt') as myfile:
    for line in myfile:
        gene_flag = re.compile('([\s]+)(/gene=")(.+)(")')
        gene_found = re.match(gene_flag,line)
        if gene_found != None:
            gene_id = gene_found.group(3)
            print(gene_id,end=',')
print('\n')
with open('genbank2.txt','rt') as myfile:
    for line in myfile:
        prot_flag = re.compile('([\s]+)(/product=")(.+)(")')
        prot_found = re.match(prot_flag,line)
        if prot_found != None:
            prot_name = prot_found.group(3)
            print(prot_name,end=',')
print('\n')
with open('genbank2.txt','rt') as myfile:
    for line in myfile:
        sour_flag = re.compile('(([\s]+)(source)([\s]+))((1..)([0-9]+))')
        sour_found = re.match(sour_flag,line)
        if sour_found != None:
            gene_span = sour_found.group(5)
            print(gene_span,end=',')
print('\n')
with open('genbank2.txt','rt') as myfile:
    for line in myfile:
        join_flag = re.compile('(([\s]+)(CDS)([\s]+))(join\()(([0-9])(.+))')
        join_found = re.match(join_flag,line)
        if join_found != None:
            exon_map = join_found.group(6)
            print(exon_map,end='')
print('\n')
with open('genbank2.txt','rt') as myfile:
    for line in myfile:
        star_flag = re.compile('([\s]+)(/codon_)((start=)([1-3]))')
        star_found = re.match(star_flag,line)
        if star_found != None:
            start_cod = star_found.group(3)
            print(start_cod,end=',')
print('\n')
gbfile = open('genbank2.txt','r')
orig_flags = re.findall(r'(ORIGIN)',gbfile.read())
for orig_flag in orig_flags:
    gene_dna = orig_flag
    print(gene_dna,end=',')
print('\n')
