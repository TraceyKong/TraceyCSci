import random
def freq(n,l):
    count = 0
    for i in l:
        if i == n: count+=1
    return count

def min(l):
    min = l[0]
    for i in l:
        if i < min: min = i
    return min

def mode1(l):
    mode_so_far = freq(l[0],l)
    mode_index = 0
    for index,value in enumerate(l):
        next_freq = freq(value,l)
        if next_freq > mode_so_far:
            mode_so_far = next_freq
            mode_index = index
    return l[mode_index]

def build_random_list(item):
    l = []
    for i in range(item):
        l.append(random.randrange(40))
    return l
