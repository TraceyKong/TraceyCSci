def rp(w):
    result = [l for l in w if l.isalpha()]
    return ''.join(result)

def bwcd(wordlist):
    d={}
    for w in set(wordlist):
        d[w] = wordlist.count(w)
    return d

def bwcff(f):
    f = open(f).read()
    l = [rp(w) for w in f.lower().split()]
    return bwcd(l)


d = bwcff("hamlet.txt")