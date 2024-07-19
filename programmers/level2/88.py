"""
혼자 놀기의 달인
"""
def get_candidate(l, cards):
    index = l
    candidate = []
    while True:
        candidate.append(index)
        next_index = cards[index]
        if next_index in candidate:
            break
        else:
            index = next_index
    return set(candidate)

def solution(cards):
    cards = [0] + cards
    length = len(cards)
    candidates = []
    candidates_length = []
    for l in range(length):
        candidate = get_candidate(l, cards)
        if candidate not in candidates:
            candidates.append(candidate)
            candidates_length.append(len(candidate))
    if length - 1 in candidates_length:
        return 0
    candidates_length.sort()
    return candidates_length[-1] * candidates_length[-2]

print(solution([8, 6, 3, 7, 2, 5, 1, 4])) # 12
print(solution([10, 5, 6, 7, 8, 9, 1, 2, 3, 4])) # 12
print(solution([2, 3, 4, 5, 6, 7, 8, 9, 10, 1]))