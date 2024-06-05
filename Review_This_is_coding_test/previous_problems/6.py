import heapq

def solution(food_times, k):
    if sum(food_times) <= k:
        return -1

    heap = []
    for i in range(len(food_times)):
        heapq.heappush(heap, (food_times[i], i + 1))

    length = len(food_times)
    previous_time = 0

    while heap:
        t = (heap[0][0] - previous_time) * length
        if t <= k:
            k -= t
            previous_time, index = heapq.heappop(heap)
            length -= 1
        else:
            index = k % length
            heap.sort(key= lambda x: x[1])
            answer = heap[index][1]
            return answer

print(solution([8, 6, 4], 15))
