"""
후보키
"""
from itertools import combinations

def solution(relation):
    rows = len(relation)
    columns = len(relation[0])

    candidates = []
    for i in range(1, columns + 1):
        candidates.extend(combinations(range(columns), i))

    uniques = []
    for case in candidates:
        tmp = [tuple(item[key] for key in case) for item in relation]
        if len(set(tmp)) == rows:
            uniques.append(case)

    answer = set(uniques)
    for i in range(len(uniques)):
        for j in range(i + 1, len(uniques)):
            if len(uniques[i]) == len(set(uniques[i]).intersection(uniques[j])):
                answer.discard(uniques[j])

    return len(answer)


print(solution(
    [
        ["100","ryan","music","2"],
        ["200","apeach","math","2"],
        ["300","tube","computer","3"],
        ["400","con","computer","4"],
        ["500","muzi","music","3"],
        ["600","apeach","music","2"]
    ]
)) # 2