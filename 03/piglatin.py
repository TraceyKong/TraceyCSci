def piglatinify(s):
    vowels = 'aeiou'
    for i in vowels:
        if s[0] == i:
            return(s+'ay')
    return(s[1:]+s[0]+'ay')
    
print(piglatinify('latin'))