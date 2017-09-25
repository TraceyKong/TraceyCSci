def comma(lst):
    for i in range(len(lst)):
        if i+1 == len(lst):
            print('and ' + lst[i],end='')
        else: print(lst[i] + ', ',end='')
        
spam = ['apples', 'bananas', 'tofu', 'cats']

comma(spam)