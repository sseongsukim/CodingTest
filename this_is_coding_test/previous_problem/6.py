import heapq

def solution(food_times, k):
    if sum(food_times) <= k:
        return -1

    heap = []
    for i in range(len(food_times)):
        heapq.heappush(heap, (food_times[i], i + 1))

    length = len(food_times)
    previous = 0
    while heap:
        t = (heap[0][0] - previous) * length
        if t <= k:
            k -= t
            previous, index = heapq.heappop(heap)
            length -= 1
        else:
            index = k % length
            heap.sort(key= lambda x: x[1])
            answer = heap[index][1]
            break

    return answer

food_times = [8, 6, 4]
k = 15
print(solution(food_times, k))