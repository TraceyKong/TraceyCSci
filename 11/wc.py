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
    for i in range(len(tf)-2):
        l.setdefault((tf[i],tf[i+1]),[])
        l[(tf[i],tf[i+1])].append(tf[i+2])
    return l

def generate_text(d,start_word,length=50):
    wordlist=[]
    next = start_word
    for i in range(length):
        wordlist.append(next)
        next = random.choice(d[next])
    return ' '.join(wordlist)

hamlet = bwcff("hamlet.txt")
g = generate_text(hamlet,'to')
