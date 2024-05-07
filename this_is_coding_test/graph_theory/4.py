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
input = sys.stdin.readline
N = int(input())
indegree = [0] * (N + 1)
cost_list = [0] * (N + 1)
graph = [[] for _ in range(N + 1)]
for i in range(1, N + 1):
    number_list = list(map(int, input().split()))
    cost_list[i] = number_list[0]
    if len(number_list) > 2:
        indegree[i] = len(number_list[1:-1])
        for n in number_list[1: -1]:
            graph[n].append(i)

q = deque()
for i in range(1, N + 1):
    if indegree[i] == 0:
        q.append(i)

result = []
while q:
    now = q.popleft()
    result.append(cost_list[now])
    for next_node in graph[now]:
        indegree[next_node] -= 1
        if indegree[next_node] == 0:
            cost_list[next_node] += cost_list[now]
            q.append(next_node)

print(result)