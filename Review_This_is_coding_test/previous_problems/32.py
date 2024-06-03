"""
5
7
3 8
8 1 0
2 7 4 4
4 5 2 6 5
"""
N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

for i in range(1, N):
    for j in range(i + 1):
        if j == 0:
            arr[i][j] += arr[i - 1][j]
        elif j == i:
            arr[i][j] += arr[i - 1][j - 1]
        else:
            arr[i][j] += max(arr[i - 1][j], arr[i - 1][j - 1])

print(max(arr[N - 1]))
