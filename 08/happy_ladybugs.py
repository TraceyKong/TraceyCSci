import sys

a = []
def play(n,b):
    if b.count('_') == 0:
        for i in range(n):
            if (i == 0 or b[i-1] != b[i]) and (i == n-1 or b[i+1] != b[i]):
                return 'NO'
        return 'YES'
    lst = {}
    for i in b:
        if i != '_':
            if i not in lst.keys(): lst.setdefault(i,1)
            else: lst[i] += 1
    for j in lst.values():
        if j<2: return 'NO'
    return 'YES'

Q = int(input().strip())
for a0 in range(Q):
    n = int(input().strip())
    b = input().strip()
    a.append(play(n,b))
    
for x in a: print(x)