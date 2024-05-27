import heapq

def solution(food_times, k):
    if sum(food_times) <= k:
        return -1

    heap = []
    for i in range(len(food_times)):
        heapq.heappush(heap, (food_times[i], i + 1))

    count = 0
    previous = 0
    length = len(food_times)
    while count + (heap[0][0] - previous) * length <= k:
        now, index = heapq.heappop(heap)
        count += (now - previous) * length
        length -= 1
        previous = now

    result = sorted(heap, key= lambda x: x[1])
    return result[(k - count) % length][1]


food_times = [8, 6, 4]
k = 15
# answer = 2
print(solution(food_times, k))