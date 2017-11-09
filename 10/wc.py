def rp(w):
    result = [l for l in w if l.isalpha()]
    return ''.join(result)


def bwcd(wordlist):
    d={}
    for w in set(wordlist):
        d[w] = wordlist.count(w)
    return d

def hbwcd(f):
    f = open(f).read()
    l = [rp(w) for w in f.lower().split()]
    return l

def bwcff(f):
    return bwcd(hbwcd(f))

def tbo(s,f):
    tf = hbwcd(f)
    st = [rp(w) for w in s.lower().split()]
    l = {}
    for w in st:
        l[w] = [tf[i+1] for i in range(len(tf)) if tf[i]==w]
    return l

d = bwcff("hamlet.txt")
t = tbo('to be or not to be',"hamlet.txt")
