"""
5
10 -1
10 1 -1
4 1 -1
4 3 1 -1
3 3 -1
"""
from collections import deque
import sys
import copy
input = sys.stdin.readline
N = int(input())
indegree = [0] * (N + 1)
costs = [0] * (N + 1)
arr = [[] for _ in range(N + 1)]
for i in range(1, N + 1):
    numbers = list(map(int, input().split()))
    costs[i] = numbers[0]
    for n in numbers[1: -1]:
        indegree[i] += 1
        arr[n].append(i)

q = deque()
for i in range(1, N + 1):
    if indegree[i] == 0:
        q.append(i)

result = copy.deepcopy(costs)
while q:
    now = q.popleft()
    for next_node in arr[now]:
        indegree[next_node] -= 1
        if indegree[next_node] == 0:
            result[next_node] = max(result[next_node], costs[next_node] + result[now])
            q.append(next_node)

print(result[1:])