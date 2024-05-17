"""
5
7
3 8
8 1 0
2 7 4 4
4 5 2 6 5
"""
import sys
input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
    numbers = list(map(int,input().split()))
    arr.append(numbers)

for i in range(1, N):
    length = len(arr[i])
    for j in range(length):
        if j == 0:
            arr[i][j] += arr[i - 1][j]
        elif j == length - 1:
            arr[i][j] += arr[i - 1][j - 1]
        else:
            arr[i][j] += max(arr[i - 1][j - 1], arr[i - 1][j])

print(max(arr[N - 1]))
