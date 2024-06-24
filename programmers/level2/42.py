"""
롤케이크 자르기

"""
from collections import Counter

def solution(topping):
    answer = 0
    brother = Counter(topping)
    chulsu = set()
    for t in topping:
        brother[t] -= 1
        if brother[t] == 0:
            del brother[t]
        chulsu.add(t)
        if len(brother) == len(chulsu):
            answer += 1
    return answer



print(solution([1, 2, 1, 3, 1, 4, 1, 2])) # 2
print(solution([1, 2, 3, 1, 4])) # 0