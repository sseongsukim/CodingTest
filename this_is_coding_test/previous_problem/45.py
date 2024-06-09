"""
3
5
5 4 3 2 1
2
2 4
3 4
3
2 3 1
0
4
1 2 3 4
3
1 2
3 4
2 3
"""
from collections import deque
import sys
input = sys.stdin.readline

TC = int(input())
for _ in range(TC):
    N = int(input())

    indegree = [0] * (N + 1)
    graph = [[False] * (N + 1) for _ in range(N + 1)]
    numbers = list(map(int, input().split()))
    for i in range(N):
        for j in range(i + 1, N):
            indegree[numbers[j]] += 1
            graph[numbers[i]][numbers[j]] = True

    C = int(input())
    for _ in range(C):
        a, b = map(int, input().split())
        if graph[a][b]:
            graph[a][b] = False
            graph[b][a] = True
            indegree[b] -= 1
            indegree[a] += 1
        else:
            graph[b][a] = False
            graph[a][b] = True
            indegree[a] -= 1
            indegree[b] += 1

        q = deque()
        for i in range(1, N + 1):
            if indegree[i] == 0:
                q.append(i)

        result = []
        certain = True
        cycle = False

        for i in range(N):
            if len(q) == 0:
                cycle = True
                break

            if len(q) > 2:
                certain = False
                break

            now = q.popleft()
            result.append(now)
            for j in range(1, N + 1):
                if graph[now][j]:
                    indegree[j] -= 1
                    if indegree[j] == 0:
                        q.append(j)

        if cycle:
            print('IMPOSSIBLE')
        elif not certain:
            print("?")
        else:
            for i in result:
                print(i, end= ' ')
            print()

