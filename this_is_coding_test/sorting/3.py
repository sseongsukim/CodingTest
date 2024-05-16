"""
2
홍길동 95
이순신 77
"""
N = int(input())
arr = []
for _ in range(N):
    name, score = input().split()
    arr.append((name, int(score)))

arr.sort(key= lambda x: x[1])
for name, score in arr:
    print(name, end= ' ')