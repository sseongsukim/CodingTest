"""
0001100
-> 1

"""
S = input()
first = S[0]

zeros = 0
ones = 0

if int(first) == 0:
    zeros += 1
else:
    ones += 1

for i in range(len(S) - 1):
    if S[i + 1] != S[i]:
        if int(S[i + 1]) == 0:
            zeros += 1
        else:
            ones += 1

print(min(zeros, ones))