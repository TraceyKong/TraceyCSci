import random

story = '''NAME is a very suave guy played by NAME. He\'s done some bad stuff, but he\'s
    very cool. He has a long conversation with a NOUN, in which he makes NUMBER  references to a classic hollywood
    film that was based on the obscure japanese film NOUN NOUN, then he kills him very violently by VERB ing
    him in the NOUN and then VERB ing his NOUN off. After making another really great reference to NOUN NOUN,
    he drives a NOUN to the home of NAME, who is played by NAME. They have another very long, wordy, sharp-tongued
    conversation in which cinematography references NOUN NOUN and the dialogue is an homage to NOUN NOUN, and then
    they get in a very bloody fight in which they VERB each other's NOUN with NOUN and talk about NOUN NOUN for a really long time.'''

nouns = ['paper', 'pony', 'blob', 'monarchy', 'brain']
names = ['Bob the Builder', 'John Smith', 'Indiana Jones']
verb = ['play', 'surf', 'ate', 'slept', 'crash', 'called', 'fried']

def return_random(l):
    return random.randrange(len(l))
    
s = story.split()
for i in range(len(s)):
    if 'NOUN' in s[i]:
        s[i] = nouns[return_random(nouns)]    
    elif 'VERB' in s[i]:
        s[i] = verb[return_random(verb)]
    elif 'NAME' in s[i]:
        s[i] = names[return_random(names)]
    elif 'NUMBER' in s[i]:
        s[i] = str(int(random.random()*1000))

s2 = ' '.join(s)
 
print(s2)

