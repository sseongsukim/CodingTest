"""
3 3
3 1 2
4 1 4
2 2 2

2 4
7 3 1 8
3 3 3 4
"""
N, M = map(int, input().split())
arr = []
values = []
for i in range(N):
    arr.append(list(map(int, input().split())))
    values.append(min(arr[i]))
print(max(values))