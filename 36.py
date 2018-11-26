import re 
s=raw_input() 
n=re.sub('[\a]+','',s) 
print(len(n)) 
