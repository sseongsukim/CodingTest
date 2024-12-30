import heapq

def solution(food_times, k):
    if sum(food_times) < k:
        return -1

    length = len(food_times)
    q = []
    for i in range(length):
        heapq.heappush(q, (food_times[i], i + 1))

    prev = 0
    while q:
        if k > (q[0][0] - prev) * length:
            k -= (q[0][0] - prev) * length
            length -= 1
            prev, _ = heapq.heappop(q)
        else:
            i = k % length
            q.sort(key= lambda x: x[1])
            return q[i][1]

print(solution([3, 1, 2], 5))
