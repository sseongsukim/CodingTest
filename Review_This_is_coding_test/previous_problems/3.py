"""
0001100
-> 1
1001001
-> 2
"""
N = input()
zero_clip = 0
one_clip = 0
if N[0] == "0":
    zero_clip += 1
else:
    one_clip += 1

for i in range(len(N) - 1):
    if N[i + 1] != N[i]:
        if N[i + 1] == "1":
            one_clip += 1
        else:
            zero_clip += 1

print(min(zero_clip, one_clip))