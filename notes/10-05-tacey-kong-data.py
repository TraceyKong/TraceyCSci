#you can read a file into a big string using read
f = open('data.txt')
s = f.read()
print(s)

s2 = open('data.txt').read()
print(s2)

s3 = open('data.txt').read()
print(s3.split('\n'))

for i in s3.split('\n'):
    print(i)