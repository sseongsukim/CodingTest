"""
우박수열 정적분
"""

def triangle(a, b):
    value = 0
    min_value = min(a, b)
    max_value = max(a, b)
    value += min_value
    value += 0.5 * (max_value - min_value)
    return value

def solution(k, ranges):
    result = [(0, k)]
    count = 1
    while k != 1:
        if k % 2 == 0:
            k /= 2
        else:
            k *= 3
            k += 1
        result.append((count, float(k)))
        count += 1

    end = result[-1][0]
    answer = []
    for left, right in ranges:
        if left == right == 0:
            value = 0
            for i in range(1, end + 1):
                value += triangle(result[i][1], result[i - 1][1])
        else:
            a = left
            b = end + right
            if a > b:
                value = -1.0
            else:
                value = 0
                for i in range(a + 1, b + 1):
                    value += triangle(result[i][1], result[i - 1][1])
        answer.append(float(value))
    return answer








print(solution(5, [[0,0],[0,-1],[2,-3],[3,-3]])) # [33.0,31.5,0.0,-1.0]
print(solution(3, [[0,0], [1,-2], [3,-3]])) # [47.0,36.0,12.0]