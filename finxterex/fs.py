fs = [
    lambda x:x+1,
    lambda x:x+x,
    lambda x:x*x
    ]

n=0

for f in fs:
    n=f(n)
    

print(n)    

print('P"yt\'h"on')

l=[[]]

if l:
    print(True)
else:
    print(False)
    
days="MonTueWedThuFriSatSun"

getDay = lambda i : days[(i-1)*3:i*3]

print(getDay(1))
print(getDay(6))

x=0
if False or [False] or (False):
    x+=1
    
print(x)

print('''\
A
B
C
''')

import re

matches = re.findall('t','Coconut')
print(matches)

result=len(matches)
print(result)
                     