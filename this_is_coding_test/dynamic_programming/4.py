"""
3 > 5
"""
N = int(input())
counts = [0] * (N + 1)

counts[1] = 1
counts[2] = 3

for i in range(3, N + 1):
    counts[i] = counts[i - 1] + counts[i - 2] * 2

print(counts)