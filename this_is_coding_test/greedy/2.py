"""
5 8 3
2 4 5 4 6
"""
N, M, K = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
answer = 0
for i in range(1, M + 1):
    if i % K == 0:
        answer += arr[-2]
    else:
        answer += arr[-1]

print(answer)