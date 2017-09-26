def string(s):
    '''
        if s = abc then return a = aababc
    '''
    l = len(s)
    result = ''
    i = 0
    while i<l:
        result+=s[:i+1]
        i+=1
    return result

def string_for(s):
    '''
        if s = abc then return a = aababc
    '''
    l = len(s)
    result = ''
    for i in range(l):
        result += s[:i+1]
    return result

print(string_for('abc'))

#================================================

