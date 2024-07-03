"""
배달

"""
from collections import deque

def solution(N, road, K):
    INF = int(1e9)
    hours = [[INF] * (N + 1) for _ in range(N + 1)]
    for start, end, hour in road:
        if hour < hours[start][end]:
            hours[start][end] = hour
            hours[end][start] = hour

    MAP = [[] for _ in range(N + 1)]
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if hours[i][j] != INF:
                MAP[i].append((j, hours[i][j]))

    start = 1
    distance = [INF] * (N + 1)
    distance[start] = 0
    q = deque()
    q.append(start)
    while q:
        now = q.popleft()
        for next_city, hour in MAP[now]:
            next_hour = distance[now] + hour
            if next_hour < distance[next_city]:
                distance[next_city] = next_hour
                q.append(next_city)
    answer = 0
    for dist in distance[1:]:
        if dist <= K:
            answer += 1
    return answer



print(solution(5, [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]], 3)) # 4
print(solution(6, [[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]], 4)) # 4