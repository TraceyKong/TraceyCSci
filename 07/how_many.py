def freq(n,l):
    count = 0
    for i in l:
        if i == n: count+=1
    return count

def min(l):
    min = l[0]
    for i in l:
        if i < min: min = i
    return min

def mode(l):
    f = []
    max = 0
    for i in range(len(l)):
        f.append(freq(l[i],l))
        if i != 0 and f[i] > f[i-1]:
            max = l[i]
    return max

def mode1(l):
    f = freq(l[0],l)
    i = 0
    for a in range(len(l)):
        c = freq(l[a],l)
        if c > f:
            f = c
            i = a
    return l[i]