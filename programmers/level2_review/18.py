"""
연속 부분 수열 합의 개수
"""
def solution(elements):
    length = len(elements)
    elements += elements
    candidates = []
    for i, e in enumerate(elements):
        print(e)
        value = e
        candidates.append(value)
        for b in elements[i + 1: i + length]:
            value += b
            candidates.append(value)
    return len(set(candidates))

print(solution([7, 9, 1, 1, 4])) # 18