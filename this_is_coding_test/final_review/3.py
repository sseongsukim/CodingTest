s = input()

num_zero = 0
num_one = 0

first = int(s[0])
if first == 0:
    num_zero += 1
else:
    num_one += 1

for i in range(1, len(s)):
    if s[i] != s[i - 1]:
        if int(s[i]) == 1:
            num_one += 1
        else:
            num_zero += 1

print(min(num_zero, num_one))