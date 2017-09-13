def string_times(str, n):
    s = ''
    for x in range(n):
        s+=str
    return s

def front_times(str, n):
    s = str[:3]
    t = ''
    for x in range(n):
        t+=s
    return t

def string_bits(str):
    s = ''
    for x in range(0,len(str),2):
        s+=str[x]
    return s

def lone_sum(a, b, c):
    lst = [a,b,c]
    sum = 0
    for x in range(len(lst)):
        s = True
        for i in range(len(lst)):
            if lst[x] == lst[i] and x != i:
                s = False
        if s: sum+=lst[x]
    return sum

def string_splosion(str):
    i = ''
    for x in range(len(str)):
        i+=str[:x+1]
    return(i)

def cigar_party(cigars, is_weekend):
    return((is_weekend and cigars >=40) or (cigars >= 40 and cigars <= 60))

def caught_speeding(speed, is_birthday):
    x = 0
    if is_birthday: x+=5
    if speed < 61+x:
        return 0
    elif speed > 80+x:
        return 2
    else:
        return 1
    
#===============================================================
print("string_times('Hi', 4) \n >>>",string_times('Hi', 4))
print("--------------- \n")
print("front_times('Chocolate',3) \n >>>",front_times('Chocolate',3))
print("--------------- \n")
print("string_bits('Hello') \n >>>",string_bits('Hello'))
print("--------------- \n")
print("lone_sum(2,3,2) \n >>>",lone_sum(2,3,2))
print("lone_sum(2,3,4) \n >>>",lone_sum(2,3,4))
print("lone_sum(3,3,3) \n >>>",lone_sum(3,3,3))
print("--------------- \n")
print("string_splosion('Code') \n >>>", string_splosion('Code'))
print("--------------- \n")
print("cigar_party(50,False) \n >>>",cigar_party(50,False))
print("cigar_party(74,False) \n >>>",cigar_party(74,False))
print("cigar_party(57,True) \n >>>",cigar_party(57,True))
print("--------------- \n")
print("caught_speeding(60, False) \n >>>",caught_speeding(60, False))
print("caught_speeding(65, False) \n >>>",caught_speeding(65, False))
print("caught_speeding(86, True) \n >>>",caught_speeding(86, True))
print("caught_speeding(85, True) \n >>>",caught_speeding(85, True))