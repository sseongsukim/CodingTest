"""
5
-> 11475
"""
N = int(input())
count = 0
for h in range(N + 1):
    for i in range(60):
        for j in range(60):
            if str(N) in str(h) + str(i) + str(j):
                count += 1

print(count)