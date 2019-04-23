import re

new_locus = False
position = 0

with open('genbank2.txt','rt') as myfile:
    for line in myfile:

        loc_flag = re.compile('(LOCUS)')
        loc_found = re.match(loc_flag,line)
        if loc_found != None:
            new_locus = True
            position = position + 1
            map_got = False
            gene_got = False
            prot_got = False
            sour_got = False
            join_got = False
            star_got = False           
            print('LOCUS' ,position, 'of 111:')
        
        acc_flag = re.compile('(ACCESSION)([\s]+)(([A-Z]+)([0-9]+))')
        acc_found = re.match(acc_flag,line)
        if acc_found != None:
            acc_code = acc_found.group(3)
            print(acc_code,end=',')

        if map_got == False:  
            map_flag = re.compile('([\s]+)(/map=")(.+)(")')
            map_found = re.match(map_flag,line)
            if map_found != None:
                map_got = True
                chrom_loc = map_found.group(3)
                print(chrom_loc,end=',')

        if gene_got == False:
            gene_flag = re.compile('([\s]+)(/gene=")(.+)(")')
            gene_found = re.match(gene_flag,line)
            if gene_found != None:
                gene_got = True                
                gene_id = gene_found.group(3)
                print(gene_id,end=',')

        if prot_got == False:
            prot_flag = re.compile('([\s]+)(/product=")(.+)(")')
            prot_found = re.match(prot_flag,line)
            if prot_found != None:
                prot_got = True
                prot_name = prot_found.group(3)
                print(prot_name,end=',')

        if sour_got == False:
            sour_flag = re.compile('(([\s]+)(source)([\s]+))((1..)([0-9]+))')
            sour_found = re.match(sour_flag,line)
            if sour_found != None:
                sour_got = True
                gene_span = sour_found.group(5)
                print(gene_span,end=',')

        if join_got == False:
            join_flag = re.compile('(([\s]+)(CDS)([\s]+))(join\()(([0-9])(.+))')
            join_found = re.match(join_flag,line)
            if join_found != None:
                join_got = True
                exon_map = join_found.group(6)
                print(exon_map,end='')

        if star_got == False:          
            star_flag = re.compile('([\s]+)(/codon_)((start=)([1-3]))')
            star_found = re.match(star_flag,line)
            if star_found != None:
                star_got = True
                start_cod = star_found.group(3)
                print(start_cod,end=',')      

        end_flag = re.compile(r'//')
        end_found = re.match(end_flag,line)
        if end_found != None:
            new_locus = False
            print('\n','NEXT ',end='')

print('\n')      
gbfile = open('genbank2.txt','r')
orig_flags = re.findall(r'(ORIGIN)',gbfile.read())
for orig_flag in orig_flags:
    gene_dna = orig_flag
    print(gene_dna,end=',')
print('\n')


            
