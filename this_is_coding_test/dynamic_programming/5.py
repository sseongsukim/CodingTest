"""
2 15
2
3

3 4
3
5
7
"""
N, M = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(int(input()))

d = [10001] * (M + 1)
d[0] = 0
for i in range(N):
    for j in range(arr[i], M + 1):

        if d[j - arr[i]] != 10001:
            d[j] = min(d[j], d[j - arr[i]] + 1)