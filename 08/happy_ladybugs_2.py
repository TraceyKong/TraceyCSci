import sys

def in_list(c,l):
    for i in range(len(l)):
        if l[i] == c: return i
    return -1

a = []
def play(n,b):
    if b.count('_') == 0:
        for i in range(n):
            if (i == 0 or b[i-1] != b[i]) and (i == n-1 or b[i+1] != b[i]):
                return 'NO'
        return 'YES'
    colors = []
    amounts = []
    for i in b:
        if i!='_':
            if in_list(i,colors)>-1:
                amounts[in_list(i,colors)]+=1
            else:
                colors.append(i)
                amounts.append(1)
    for i in amounts:
        if i < 2: return 'NO'
    return 'YES'

Q = int(input().strip())
for a0 in range(Q):
    n = int(input().strip())
    b = input().strip()
    a.append(play(n,b))
    
for x in a: print(x)
