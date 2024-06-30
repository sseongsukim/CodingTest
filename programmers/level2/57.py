"""
두 큐 합 같게 만들기
sum() is a time-consuming process
"""
from collections import deque

def solution(queue1, queue2):
    q1_sum = sum(queue1)
    total = q1_sum + sum(queue2)
    target = int(total / 2)
    q1 = deque(queue1)
    q2 = deque(queue2)
    count = 0
    while q1_sum != target:
        if q1_sum < target:
            q2_value = q2.popleft()
            q1.append(q2_value)
            q1_sum += q2_value
        elif q1_sum > target:
            q1_value = q1.popleft()
            q2.append(q1_value)
            q1_sum -= q1_value
        count += 1
        if count >= len(queue1) * 3:
            return -1
    return count


print(solution([3, 2, 7, 2], [4, 6, 5, 1])) # 2
print(solution([1, 2, 1, 2], [1, 10, 1, 2])) # 7
print(solution([1, 1], [1, 5])) # -1
print(solution([1, 1, 1, 1], [1, 1, 7, 1])) # 9
print(solution([10, 5, 1], [2, 2, 2])) # -1
