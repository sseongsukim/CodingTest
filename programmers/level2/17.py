"""
연속 부분 수열 합의 개수

list -> set
"""


def solution(elements):
    answer = []
    max_length = len(elements)
    new_elements = elements + elements
    for i, e in enumerate(new_elements):
        sums = e
        answer.append(sums)
        for b in new_elements[i + 1: i + max_length]:
            sums += b
            answer.append(sums)

    print(answer)
    print(set(answer))
    return len(set(answer))



print(solution([7, 9, 1, 1, 4])) # 18
