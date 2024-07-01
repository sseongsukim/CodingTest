"""
전력망을 둘로 나누기

"""
from collections import deque

def solution(n, wires):
    MAP = [[] for _ in range(n + 1)]
    for x, y in wires:
        MAP[x].append(y)
        MAP[y].append(x)

    def count_city(start, end):
        visited = [False] * (n + 1)
        visited[start] = True
        q = deque()
        q.append(start)
        num_cities = 1
        while q:
            current_city = q.popleft()
            for next_city in MAP[current_city]:
                if next_city != end:
                    if not visited[next_city]:
                        q.append(next_city)
                        num_cities += 1
                        visited[next_city] = True
        return num_cities

    answer = 1e9
    for city in range(1, n + 1):
        for other_city in MAP[city]:
            a = count_city(city, other_city)
            b = count_city(other_city, city)
            answer = min(answer, abs(a - b))
    return answer





print(solution(9, [[1, 3],[2, 3],[3, 4],[4, 5],[4, 6],[4, 7],[7, 8],[7, 9]])) # 3
print(solution(4, [[1, 2], [2, 3], [3, 4]])) # 0
print(solution(7, [[1, 2], [2, 7], [3, 7], [3, 4], [4, 5], [6, 7]])) # 1