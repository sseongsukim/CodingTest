"""
메뉴 리뉴얼

"""
from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    for l in course:
        candidates = []
        for order in orders:
            for case in list(combinations(order, l)):
                candidate = "".join(sorted(case))
                candidates.append(candidate)
        candidates = Counter(candidates).most_common()
        if len(candidates) == 0:
            break
        max_value = candidates[0][1]
        for candidate, num in candidates:
            if num == max_value and num > 1:
                answer.append(candidate)
    answer.sort()
    return answer


print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4])) # ["AC", "ACDE", "BCFG", "CDE"]
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2, 3, 5])) # ["ACD", "AD", "ADE", "CD", "XYZ"]
print(solution(["XYZ", "XWY", "WXA"], [2, 3, 4])) # ["WX", "XY"]