'''
Instructions from your teacher:
In the game of scrabble, letters are scored as follows:


Letter                             Value
A, E, I, O, U, L, N, R, S, T       1
D, G                               2
B, C, M, P                         3
F, H, V, W, Y                      4
K                                  5
J, X                               8
Q, Z                               10



Write a routine score(w) which will return the scrabble score for the word specified by the string w.

For example, score("hello") will return 8 since h is worth 4 points and each of the other letters is worth 1.

For full credit you should use the appropriate Python constructs to represent the scores
'''

values = {1:'aeioulnrst',2:'dg',3:'bcmp',4:'fhvwy',5:'k',8:'jx',10:'qz'}

def score(w):
  s = 0
  for i in w.lower():
    for c in values.keys():
      if i in values[c]:
        s+=c
  return s
  
print('score("hello") >>>',score('hello'))
print('score("tracey") >>>',score('tracey'))
print('score("are") >>>',score('are'))