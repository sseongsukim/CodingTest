"""
택배상자
Stack !
"""
def solution(order):
    extra_container = []
    b_index = 0
    o_index = 0
    for i in range(1, len(order) + 1):
        extra_container.append(i)
        while extra_container and extra_container[-1] == order[o_index]:
            extra_container.pop()
            o_index += 1
            b_index += 1
    return o_index


print(solution([4, 3, 1, 2, 5])) # 2
print(solution([5, 4, 3, 2, 1])) # 5