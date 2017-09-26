l='a'
print(ord(l))

for letter in "abcdefg":
    ascii_val = ord(letter)
    plus = ascii_val + 3
    newchar = chr(plus)
    print(letter,":",ascii_val," rotated: ",newchar,':',plus)