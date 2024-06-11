
def solution(brown, yellow):
    total_boxes = brown + yellow
    for a in range(1, total_boxes + 1):
        b = total_boxes / a
        if b % 1 == 0:
            if (a - 2) * (b - 2) == yellow:
                return [int(b), a]

print(solution(10, 2)) # [4, 3]
print(solution(8, 1)) # [3, 3]
print(solution(24, 24)) # [8, 6]