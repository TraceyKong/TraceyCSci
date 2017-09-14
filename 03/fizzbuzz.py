'''
    Write a program that prints the numbers from 1 to 100.
    But for multiples of three print “Fizz” instead of the
    number and for the multiples of five print “Buzz”. For
    numbers which are multiples of both three and five print “FizzBuzz”.
'''

def fizzbuzz():
    x = 1
    result = []
    while x < 101:
        if x%3 == 0:
            if x%5 == 0:
                result.append('FizzBuzz')
            else:
                result.append('Fizz')
        elif x%5 == 0:
            result.append('Buzz')
        else:
            result.append(x)
        x+=1
    return result

answer = fizzbuzz()

for i in range(len(answer)):
    if (i+1)%10 == 0:
        print(str(answer[i])+'\n')
    else: print(str(answer[i]),' ',end='')