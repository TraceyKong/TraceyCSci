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
        a,b,c = tf[i],tf[i+1],tf[i+2]
        l.setdefault((a,b),[])
        l[(a,b)].append(c)
    return l

def generate_text(d,length=50):
    k = list(d.keys())
    next = random.choice(k)
    text_list = list(next)
    for i in range(length):
        next_word = random.choice(d[next])
        if next_word == '':
            break
        next = next[1:] + (next_word,)
        print(next)
        text_list.append(next_word)
    return ' '.join(text_list)
    
def build_ngrams(wordlist,prelength):
    d={}
    for i in range(len(wordlist)-prelength+1):
        sublist = worldList[i:i+prelength+1]
        t = tuple(sublist[0:len(sublist)])

hamlet = bwcff("hamlet.txt")