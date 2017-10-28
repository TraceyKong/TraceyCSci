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

def decode(lst):
    s = ''
    i = 0
    while i < len(lst):
        if isinstance(lst[i],int):
            s+=lst[i+1]*lst[i]
            i+=1
        else:
            s+=lst[i]
        i+=1
    return s

print(decode(encode('aabbbcdd')))