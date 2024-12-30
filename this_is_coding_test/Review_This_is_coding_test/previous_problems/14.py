from itertools import permutations

def solution(n, weak, dist):
    answer = len(dist) + 1
    length = len(weak)
    for i in range(length):
        weak.append(n + weak[i])
    for i in range(length):
        for case in permutations(dist, len(dist)):
            count = 1
            position = weak[i] + case[count - 1]
            for idx in range(i, i + length):
                if position < weak[idx]:
                    count += 1
                    if count > len(dist):
                        break
                    position = weak[idx] + case[count - 1]
        answer = min(answer, count)
    return answer


print(solution(12, [1, 5, 6, 10], [1, 2, 3, 4]))
print(solution(12, [1, 3, 4, 9, 10], [3, 5, 7]))