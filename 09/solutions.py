def divide(A,B,u):
    return int(u/(A/B))

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
  
values = {1:'aeioulnrst',2:'dg',3:'bcmp',4:'fhvwy',5:'k',8:'jx',10:'qz'}

def score(w):
  s = 0
  for i in w.lower():
    for c in values.keys():
      if i in values[c]:
        s+=c
  return s
