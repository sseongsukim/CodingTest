"""
2
홍길동 95
이순신 77
"""
N = int(input())
arr = []
for i in range(N):
    name, score = input().split()
    arr.append((int(score), name))

arr.sort(key= lambda x: x[0])
for answer in arr:
    print(answer[1], end= ' ')