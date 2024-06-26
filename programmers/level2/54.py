"""
다리를 지나는 트럭

"""
from collections import deque

def solution(bridge_length, weight, truck_weights):
    times = 2
    order = 1
    on_bridge = deque([])
    on_bridge.append([1, truck_weights[0]])
    while True:
        if order < len(truck_weights):
            if sum([x[1] for x in on_bridge]) + truck_weights[order] <= weight:
                on_bridge.append([0, truck_weights[order]])
                order += 1

        if len(on_bridge):
            for i in range(len(on_bridge)):
                on_bridge[i][0] += 1

        if len(on_bridge):
            if on_bridge[0][0] == bridge_length:
                on_bridge.popleft()

        times += 1
        if order == len(truck_weights) and not on_bridge:
            break

    return times


print(solution(2, 10, [7, 4, 5, 6])) # 8
print(solution(100, 100, [10])) # 101
print(solution(100, 100, [10,10,10,10,10,10,10,10,10,10])) # 110