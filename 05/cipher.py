def encode_letter(c,r):
    a = 65
    if ord(c)>=97:
        a = 97
    return chr(((ord(c)-a)+r)%26+a)

def encode_string(s,r):
    answer = ''
    for letter in s:
        if letter.isalpha():
            answer+=encode_letter(letter,r)
        else: answer+=letter
    return answer

def full_encode(s):
    answer=[]
    for i in range(1,26):
        a = encode_string(s,i)
        answer.append(a)
    print('\n'.join(answer))