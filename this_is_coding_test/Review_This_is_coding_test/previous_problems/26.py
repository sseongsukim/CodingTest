import heapq

N = int(input())
numbers = []
for _ in range(N):
    heapq.heappush(numbers, int(input()))
answer = 0
while len(numbers) != 1:
    left = heapq.heappop(numbers)
    right = heapq.heappop(numbers)
    summation = (left + right)
    heapq.heappush(numbers, summation)
    answer += summation
print(answer)