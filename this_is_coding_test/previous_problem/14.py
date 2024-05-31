from itertools import permutations

def solution(n, weak, dist):
    answer = len(dist) + 1
    length = len(weak)
    for i in range(length):
        weak.append(n + weak[i])

    for i in range(length):
        for case in list(permutations(dist, len(dist))):

            count = 1
            position = weak[i] + case[count - 1]

            for index in range(i, i + length):
                if position < weak[index]:
                    count += 1
                    if count > len(dist):
                        break
                    position = weak[index] + case[count - 1]

        answer = min(answer, count)
    return answer

print(solution(n = 12,
               weak= [1, 5, 6, 10],
               dist = [1, 2, 3, 4]))

print(solution(n = 12,
               weak= [1, 3, 4, 9, 10],
               dist = [3, 5, 7]))