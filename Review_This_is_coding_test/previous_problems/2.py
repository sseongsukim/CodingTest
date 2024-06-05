"""
02984
-> 576
567
-> 210
5024
-> 40
"""
N = input()

answer = int(N[0])

for n in N[1:]:
    if int(n) < 1 or answer < 1:
        answer += int(n)
    else:
        answer *= int(n)

print(answer)