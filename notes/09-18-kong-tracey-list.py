l = []
l2 = [1,2,3]

l3 = ['a','b','c','d','e','f','g']
print(len(l3))
print(l3[3])

l4 = l3[2:5]
print(l4)

s = 'abcdefg'
print(s[2:5])

l.append('hello')
l.append(9)
print(l)
l.append(l2)

l3 = ['a','b','c']
l4 = [1,2,3,4,5]
longlist = l3+l4

for i in longlist:
    print(i)

'''another method
x = 0
while x<len(longlist):
    print(longlist[x])
    x+=1
'''
 
s = 'everybody has a plan until they get punched in the face'

'''
for i in s:
    print(i)
'''