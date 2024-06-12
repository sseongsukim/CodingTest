"""
Least common multiple

"""
def solution(arr):
    max_value = max(arr)
    while True:
        count = 0
        for a in arr:
            if max_value % a == 0:
                count += 1
            else:
                break
        if len(arr) == count:
            break
        max_value += 1
    return max_value


print(solution([2, 6, 8, 14])) # 168
print(solution([1, 2, 3])) # 6