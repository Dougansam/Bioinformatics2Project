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
'''
# Open file
  f = open('test.txt', 'r')
  # Feed the file text into findall(); it returns a list of all the found strings
  strings = re.findall(r'some pattern', f.read())
  k2 = re.findall(r"^\w", xx, re.MULTILINE)
((?:[A-Z]+\n)+)
with open('numbers.txt', 'r') as f:
numbers = f.readlines()
('ACCESSION', '   ', 'AB034984', 'AB', '034984')
['t', 'a', ' ', 't', 't', 'c'], ['a', 't', 't', 't', 't', 't', 'g'],
('(ORIGIN)([\s]+([A-Z0-9\s]+)(//))(ORIGIN)[\s]+(.+)\n[\s]*([0-9]
'''
