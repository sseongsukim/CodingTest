"""
연속된 부분 수열의 합
"""
def solution(sequence, k):
    l, r = 0, 0
    length = len(sequence)
    answer = []
    summation = sum(sequence[l: r + 1])
    while True:
        if summation < k:
            r += 1
            if r == length:
                break
            summation += sequence[r]
        else:
            if summation == k:
                answer.append((l, r))
            summation -= sequence[l]
            l += 1
    if len(answer) == 1:
        return list(answer[0])
    else:
        answer.sort(key= lambda x: (x[1] - x[0], x[0]))
        return list(answer[0])


print(solution([1, 2, 3, 4, 5], 7)) # [2, 3]
print(solution([1, 1, 1, 2, 3, 4, 5], 5)) # [6, 6]
print(solution([2, 2, 2, 2, 2], 6)) # [0, 2]