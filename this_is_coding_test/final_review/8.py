# K1KA5CB7
s = input()
alphabets = []
digits = 0
for i in range(len(s)):
    if s[i].isdigit():
        digits += int(s[i])
    else:
        alphabets.append(s[i])
alphabets.sort()
for alphabet in alphabets:
    print(alphabet, end='')
print(digits)