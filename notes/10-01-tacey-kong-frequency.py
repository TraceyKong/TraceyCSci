import math

def rotate_char(c,r):
    '''
    Rotates character c by amount r, wraps if past z.
    '''
    v = ord(c)
    v = v-97
    v = (v+r)%26
    v = v+97
    result = chr(v)
    return result
    
def rotate_string(s,r):
    result = ''
    for letter in s:
        if letter.isalpha():
            letter = rotate_char(letter,r)
            result+=letter
    return result
    
def distance(l1, l2):
    '''
    Euclidean distance between l1 and l2. If the lists are at different lengths,
    go to the length of the shorter list
    '''
    length = len(l2)
    if len(l1)<len(l2):
        length=len(l1)
    sum = 0
    for i in range(length):
        sum = sum+math.pow(l1[i] - l2[i],2)
        
    d = math.sqrt(sum)
    print(d)
    
def build_frequency_vector(s):
    # count the letters in the string
    # count each letter to see how many times in appears
    spaces = s.count(" ")
    num_letters = len(s) - spaces
    v = []
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        v.append((s.count(letter)/num_letters)*100)
    return v
    
def print_frequency_table(f):
    for i in range(26):
        print(chr(i+97)+':'+str(f[i]))
    
p=build_frequency_vector('hello, this is a robot.')
print_frequency_table(p)
