import random

def build_rangelist(length=10):
  l=[]
  lowval = 5
  
  for i in range(length):
    r = [lowval, lowval+random.randrange(1,20)]
    l.append(r)
    lowval = r[1] + random.randrange(1,20)
  return l
  
rangelist = build_rangelist()

def overlap(t1,t2):
  return t2[1]-t2[0] >= t2[1]-t1[1]
  
def merge(t1,t2):
  return [min(t1[0],t2[0]),max(t1[1],t2[1])]
  
def add_range(ranglist,newmerge):
  notAdded = True
  nlist = []
  for i in ranglist:
    if overlap(newmerge,i):
      nlist.append(merge(newmerge,i))
      notAdded = False
    elif newmerge[1]<i[0] and notAdded:
      nlist.append(newmerge)
      nlist.append(i)
      notAdded = False
    else: nlist.append(i)
  return nlist
    
  
print(overlap([1,5],[1,5]))
print(overlap([1,5],[2,6]))
print(overlap([2,4],[1,100]))
print(overlap([2,4],[5,10]))
print(merge([1,5],[2,7]))
print(merge([6,20],[5,10]))
print(merge([20,30],[10,50])) 
print(add_range(rangelist, [1,7]))