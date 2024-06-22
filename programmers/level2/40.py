"""
더 맵게

"""
import heapq


def solution(scoville, K):
    heap = []
    for s in scoville:
        heapq.heappush(heap, s)
    answer = 0
    while len(heap) != 1:
        one = heapq.heappop(heap)
        two = heapq.heappop(heap)
        mix = one + (two * 2)
        heapq.heappush(heap, mix)
        answer += 1
        if all(h > K for h in heap):
            break

    return answer

print(solution([1, 2, 3, 9, 10, 12], 7)) # 2