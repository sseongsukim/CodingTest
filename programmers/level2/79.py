"""
디펜스 게임

"""
import heapq
def solution(n, k, enemy):
    heap = []
    for i, e in enumerate(enemy):
        heapq.heappush(heap, e)
        if len(heap) > k:
            pop = heapq.heappop(heap)
            n -= pop
        if n < 0:
            return i
    return len(enemy)


print(solution(7, 3, [4, 2, 4, 5, 3, 3, 1])) # 5
print(solution(10, 3, [8, 8, 1, 2, 3, 4, 5, 6])) # 7
# print(solution(2, 4, [3, 3, 3, 3])) # 4