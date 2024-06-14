"""
귤 고르기

combinations -> Time over
Counter -> Make dictionary
"""
from collections import Counter

def solution(k, tangerine):
    count = 0
    answer = 0
    for v in sorted(Counter(tangerine).values(), reverse= True):
        count += v
        answer += 1
        if count >= k:
            return answer

print(solution(6, [1, 3, 2, 5, 4, 5, 2, 3])) # 3
print(solution(4, [1, 3, 2, 5, 4, 5, 2, 3])) # 2
print(solution(2, [1, 1, 1, 1, 2, 2, 2, 3])) # 1