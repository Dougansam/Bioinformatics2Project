import re
with open('genbank2.txt','rt') as myfile:
    for line in myfile: 
        acc_flag = re.compile('(ACCESSION)([\s]+)(([A-Z]+)([0-9]+))')
        acc_found = re.match(acc_flag,line)
        if acc_found != None:
            acc_code = acc_found.group(3)
            print(acc_code,end=',')
            
f = open('genbank2.txt','rt')
acc_found = re.findall(r'(ORIGIN)[\s*]+1[\s]([a-z\s]+)',f.read())
if acc_found != None:
    print(acc_found,end=',')

f = open('genbank2.txt','rt')
acc_found = re.findall(r'(ORIGIN)[\s*]+1[\s]([a-z]+[\s]+)',f.read())
if acc_found != None:
    print(acc_found,end=',')
    
f = open('genbank2.txt','rt')
acc_found = re.findall(r'(ORIGIN)[\s*]+1[\s]([a-z]+)[\s]+([a-z]+)[\s]+([a-z]+)[\s]+',f.read())
if acc_found != None:
    print(acc_found,end=',')
