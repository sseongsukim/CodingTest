"""
하노이의 탑

"""

def hnoi(floor, origin, destination):
    result = []
    mid = 6 - origin - destination
    if floor > 1:
        result += hnoi(floor - 1, origin, mid)
        result += [[origin, destination]]
        result += hnoi(floor - 1, mid, destination)
        return result
    else:
        return [[origin, destination]]

def solution(n):
    return hnoi(n, 1, 3)


print(solution(2)) # [[1, 2], [1, 3], [2, 3]]