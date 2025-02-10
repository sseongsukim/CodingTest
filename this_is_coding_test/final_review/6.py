import heapq

def solution(food_times, k):
    if sum(food_times) < k:
        return -1
    q = []
    length = len(food_times)
    for i in range(length):
        heapq.heappush(q, (food_times[i], i + 1))
    previous = 0
    while q:
        if k > (q[0][0] - previous) * length:
            k -= (q[0][0] - previous) * length
            length -= 1
            previous, _ = heapq.heappop(q)
        else:
            i = k % length
            q.sort(key=lambda x:x[1])
            return q[i][1]
print(solution([3, 1, 2], 5)) # 1
