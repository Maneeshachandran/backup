import re

email='From abc.xyz@pqr.com Mon Dec 29 01:12:15 2016'
matchEmail=re.search(r'\w+@\w+.\w+',email)
matchDomain=re.search(r'@\w+',email)
matchTime=re.search(r'^\d{2}:+\d{2}:+\d{2}',email)
print(matchTime)
if matchEmail:
   print ("Email : ", matchEmail.group())
else:
   print ("No match!!")
if matchDomain:
   print ("Time : ", matchDomain.group())
else:
   print ("No match!!")