import random

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
    tf = [rp(w) for w in f.lower().split()]
    l = {}
    for i in range(len(tf)-1):
        l.setdefault(tf[i],[])
        l[tf[i]].append(tf[i+1])
    return l

def generate_text(d,start_word,length=50):
    wordlist=[]
    next = start_word
    for i in range(length):
        wordlist.append(next)
        next = random.choice(d[next])
    return ' '.join(wordlist)

hamlet = bwcff("hamlet.txt")
psalms = bwcff("psalms.txt")
sonnets = bwcff("sonnets.txt")
g = generate_text(sonnets,'to')