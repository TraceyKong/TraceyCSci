def collatz(number):
    if number%2 == 0:
        print(number//2)
        return number//2
    else:
        print(3*number+1)
        return 3*number+1

def isNumber(a):
    if a.isdigit(): return True
    else:
        try:
            float(a)
            return True
        except ValueError:
            return False


while True:
    n = input('Enter number:')
    if isNumber(n):
        n = int(float(n))
        while n!=1:
            n=collatz(n)
        break
    else:
        print('I don\'t understand, please try again.')
        