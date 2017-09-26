'''
import random

for i in range(18):
    print(random.randrange(50))
    
l = [1,2,3,4,5]
print(l)
random.shuffle(l)
print(l)

print(random.randrange(10))
'''
#from random import randrange

#from rangom import * imports everything
#if the second module imported happen to have the same function then this would not be a
#good idea.

import random as r
#you may also rename it or assign it to a variable

print(r.randrange(20))
s='one two three'
print(s.split())

