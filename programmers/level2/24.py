"""
[1차] 캐시

"""
from collections import deque

def solution(cacheSize, cities):
    if cacheSize == 0:
        return len(cities) * 5
    for i in range(len(cities)):
        cities[i] = cities[i].lower()
    answer = 0
    q = deque([])

    for city in cities:
        if city not in q:
            q.append(city)
            answer += 5
            if len(q) > cacheSize:
                q.popleft()
        else:
            q.remove(city)
            q.append(city)
            answer += 1
            if len(q) > cacheSize:
                q.popleft()

    return answer

print(
    solution(
        cacheSize= 3,
        cities= ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"],
    )
) # 50
print(
    solution(
        cacheSize= 3,
        cities= ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"],
    )
) # 21
print(
    solution(
        cacheSize= 5,
        cities= ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"],
    )
) # 52