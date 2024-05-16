"""
3
15
27
12
"""
N = int(input())
arr = []
for _ in range(N):
    arr.append(int(input()))

arr.sort(reverse= True)

for a in arr:
    print(a, end= ' ')