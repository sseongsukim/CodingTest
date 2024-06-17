"""
피로도

"""
from itertools import permutations
import copy
def solution(k, dungeons):
    max_value = -1e9
    for cases in list(permutations(dungeons, len(dungeons))):
        count = 0
        new_k = copy.deepcopy(k)
        for minimum, use in cases:
            if new_k >= minimum:
                new_k -= use
                count += 1
            else:
                break
        max_value = max(max_value, count)
    return max_value

print(solution(80, [[80, 20], [50, 40], [30, 10]])) # 3