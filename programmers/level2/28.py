"""
프로세스

any !
"""
from collections import deque

def solution(priorities, location):
    answer = 0
    data = deque(enumerate(priorities))
    while data:
        number, priority = data.popleft()
        if any(priority < p for _, p in data):
            data.append((number, priority))
        else:
            answer += 1
            if number == location:
                return answer

print(solution([2, 1, 3, 2], 2)) # 1
print(solution([1, 1, 9, 1, 1, 1], 0)) # 5