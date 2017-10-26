'''
Run length encoding is a form of compression that is sometimes used for images or other data that's repetitive.

In run length encoding, repeated sequences of values are replaced with a count and a single value.

We are going to use run length encoding to encode a string into a list.

For example, the string "aaaaa" would encode to [5, 'a'] since a appears 5 times.

The string "bbaaa" would encode to [2,'b',3,'a'] since b occurs twice and a once.

A single letter just gets encoded as is without a count so the string "aabcccdeeeeaaa" encodes to
[2,'a',b,3,'c',d,4,'e',3,'a'].


Write a routine encode(s) which will run length encode the string s as specified above
'''

def encode2(str):
    s = []
    for i in set(str):
        if str.count(i)>1:
            s.append(str.count(i))
        s.append(i)
    return s

def encode(str):
  s = {}
  for i in str:
    s.setdefault(i,0)
    s[i]+=1
  a = []
  for c in s.keys():
    if s[c]>1:
      a.append(s[c])
    a.append(c)
  return a
  
print('encode("aaaaa") >>>',encode('aaaaa'))
print('encode("bbaaa") >>>',encode('bbaaa'))
print('encode("aabcccdeeeeaaa") >>>',encode('aabcccdeeeeaaa'))        