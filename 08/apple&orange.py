import sys

s,t = input().strip().split(' ')
s,t = [int(s),int(t)]
a,b = input().strip().split(' ')
a,b = [int(a),int(b)]
m,n = input().strip().split(' ')
m,n = [int(m),int(n)]
apple = [int(apple_temp) for apple_temp in input().strip().split(' ')]
orange = [int(orange_temp) for orange_temp in input().strip().split(' ')]

x = 0
y = 0

for i in range(m):
    p = a+apple[i]
    if p>=s and p<=t: x+=1
print(x)
for j in range(n):
    p = b+orange[j]
    if p>=s and p<=t: y+=1
print(y)    