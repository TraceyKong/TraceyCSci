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