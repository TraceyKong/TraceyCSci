import math

def encode_letter(c,r):
    a = 65
    if ord(c)>=97: a = 97
    return chr(((ord(c)-a)+r)%26+a)

def encode_string(s,r):
    answer = ''
    for letter in s:
        if letter.isalpha():
            answer+=encode_letter(letter,r)
        else: answer+=letter
    return answer

def full_encode(s):
    answer=[]
    for i in range(1,26):
        a = encode_string(s,i)
        answer.append(a)
    return answer

def distance(l1, l2):
    length = len(l2)
    if len(l1)<len(l2):
        length = len(l1)
    sum = 0
    for i in range(length):
        sum = sum + math.pow(l1[i] - l2[i],2)
    return math.sqrt(sum)

def build_frequency_vector(s):
    spaces = s.count(" ")
    num_letters = len(s) - spaces
    v = []
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        v.append((s.count(letter)/num_letters))
    return v

def print_frequency_table(f):
    for i in range(26):
        print(chr(i+97)+':'+str(f[i]))

def decode_string(s):
    combos = full_encode(s)
    distances = []
    for c in combos:
        f = build_frequency_vector(c)
        distances.append(distance(f, al_frequency))
    return combos[get_minimum(distances)]

def get_minimum(numl):
    a = 0
    m = 0
    min = numl[0]
    while a < len(numl):
        if numl[a] < min:
            min = numl[a]
            m = a
        a+=1
    return m

def print_vectors(s):
    combos = full_encode(s)
    vectors = []
    for c in combos:
        vectors.append(build_frequency_vector(c))
    for i in vectors:
        for j in i:
            print("%.2f" % j + ', ',end='')
        print('\n')
        
f = open('pg1661.txt').read()

def build_stats(t):
    text = t.lower()
    return build_frequency_vector(text)

real_stats = build_stats(f)