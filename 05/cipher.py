def encode_letter(c,r):
    return str(chr(ord(c)+r))

def encode_string(s,r):
    answer = ''
    for letter in s:
        if letter.isalpha():
            if ord(letter.upper())+r > 90:
                answer+=encode_letter(letter,r-26)
            else: answer+=encode_letter(letter,r)
        else: answer+=letter
    return answer

def full_encode(s):
    answer=[]
    for i in range(1,26):
        a = encode_string(s,i)
        answer.append(a)
    print('\n'.join(answer))
