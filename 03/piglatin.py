'''
Rules for piglatin are:
1.If the first letter is a consonant, return a new string formed by
removing the first letter, adding it to the end and then adding
"ay" so latin shoudl become atinlay.
2.If the first letter is a vowel, just add "ay" to the end of the
word.
'''
import sys

def piglatinify(s):
    if s[0] in 'aeiou':
        return(s+'ay')
    return (s[1:]+s[0]+'ay')

def run():
    str = input('Please enter a string of your choice: ')
    print(piglatinify(str)+'\n')
    
def ask():
    return input('Run again or exit? [R/E]: ')

run()
while True:
    re = ask()
    if re == 'E': break
    elif re != 'R':
        print('Sorry, I don\'t understand.')
    else:run()
