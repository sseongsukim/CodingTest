"""
7 8
1 2
1 5
2 3
2 6
3 4
4 7
5 6
6 4
"""
from collections import deque
N, M = map(int, input().split())
indegree = [0] * (N + 1)
arr = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    indegree[b] += 1
    arr[a].append(b)

q = deque()
stack = []
for i in range(1, N + 1):
    if indegree[i] == 0:
        q.append(i)
        stack.append(i)

while q:
    now = q.popleft()
    for next_node in arr[now]:
        indegree[next_node] -= 1
        if indegree[next_node] == 0:
            q.append(next_node)
            stack.append(next_node)

for s in stack:
    print(s, end= ' ')