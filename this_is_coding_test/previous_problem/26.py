"""
3
10
20
40
"""
import heapq
N = int(input())
heap = []
for _ in range(N):
    number = int(input())
    heapq.heappush(heap, number)

answer = 0
while len(heap) != 1:
    one = heapq.heappop(heap)
    two = heapq.heappop(heap)
    summation = one + two
    answer += summation
    heapq.heappush(heap, summation)

print(answer)