'''
Rules for piglatin are:
1.If the first letter is a consonant, return a new string formed by
removing the first letter, adding it to the end and then adding
"ay" so latin shoudl become atinlay.
2.If the first letter is a vowel, just add "ay" to the end of the
word.
'''
def piglatinify(s):
    vowels = 'aeiou'
    for i in vowels:
        if s[0] == i:
            return(s+'ay')
    return(s[1:]+s[0]+'ay')
    
print(piglatinify('latin'))