"""
4
5 1 7 9
"""
N = int(input())
arr = sorted(list(map(int, input().split())))

print(arr[(N - 1) // 2])