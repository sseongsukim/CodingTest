"""
구멍보트
"""
from collections import deque

def solution(people, limit):
    people.sort()
    people = deque(people)
    answer = 0
    while len(people) > 1:
        if people[0] + people[-1] > limit:
            answer += 1
            people.pop()
        else:
            answer += 1
            people.pop()
            people.popleft()
    if len(people) == 1:
        answer += 1
    return answer


print(solution([70, 50, 80, 50], 100)) # 3
print(solution([70, 80, 50], 100)) # 3
