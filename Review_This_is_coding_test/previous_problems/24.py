"""
4
5 1 7 9
-> 5
"""
N = int(input())
numbers = sorted(list(map(int, input().split())))
print(numbers[(N - 1) // 2])