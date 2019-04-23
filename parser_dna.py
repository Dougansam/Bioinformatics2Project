import re

f = open('genbank2.txt','rt')
dna_found = re.findall\
(r'(ORIGIN)[\s*]+1[\s]([a-z\s0-9]+)[\s]([a-z\s]+)[\s*]([//])',f.read())
if dna_found != None:
    print(dna_found,end=',')




'''
Known issues:

1. Currently, output needs trimming to remove extraneous upper case letters,
numbers, white space and brackets.

'''
