"""


"""
from collections import deque

def solution(people, limit):
    answer = 0
    people.sort()
    people = deque(people)
    while len(people) > 1:
        if people[0] + people[-1] <= limit:
            answer += 1
            people.pop()
            people.popleft()
        else:
            answer += 1
            people.pop()
    if len(people) == 1:
        answer += 1
    return answer


print(solution([70, 50, 80, 50], 100))
print(solution([70, 80, 50], 100))
print(solution([30, 30, 30, 30, 80], 100))