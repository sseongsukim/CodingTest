"""
0001100
-> 1

"""
S = input()
first = S[0]
flip_zero = 0
flip_one = 0
if first == '0':
    flip_zero += 1
else:
    flip_one += 1

for i in range(len(S) - 1):
    if S[i] != S[i + 1]:
        if S[i + 1] == '0':
            flip_zero += 1
        else:
            flip_one += 1

print(flip_zero, flip_one)