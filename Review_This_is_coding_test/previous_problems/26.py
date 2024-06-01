"""
3
10
20
40
-> 100

4
1
2
4
5
-> 22
"""
import heapq
N = int(input())
data = []
for _ in range(N):
    number = int(input())
    heapq.heappush(data, number)

answer = 0
while len(data) != 1:
    one = heapq.heappop(data)
    two = heapq.heappop(data)
    plus = one + two
    answer += plus
    heapq.heappush(data, plus)

print(answer)