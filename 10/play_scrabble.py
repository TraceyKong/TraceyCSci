import scrabble

values = {1:'aeioulnrst',2:'dg',3:'bcmp',4:'fhvwy',5:'k',8:'jx',10:'qz'}

def score(w,r,c,d):
    s = 0
    t = 0
    for i in w.lower():
        for k in values.keys():
            if i in values[k]:
                if (r,c) in scrabble.TRIPLE_WORD_SCORE:t+=3
                elif (r,c) in scrabble.DOUBLE_WORD_SCORE: t+=2
                elif (r,c) in scrabble.TRIPLE_LETTER_SCORE: s+=k*2
                elif (r,c) in scrabble.DOUBLE_LETTER_SCORE: s+=k
                s+=k
                if d: c+=1
                else: r+=1
    if t>0: return t*s
    return s
        
def add_word_across(board,word,r,c):
    s = score(word,r,c,True)
    for i in word:
        board[r][c]=i
        c+=1
    scrabble.print_board(board)
    b=board
    return s

def add_word_down(board,word,r,c):
    s = score(word,r,c,False)
    for i in word:
        board[r][c]=i
        r+=1
    scrabble.print_board(board)
    b=board
    return s

b = scrabble.make_scrabble_board()
scrabble.print_board(b)