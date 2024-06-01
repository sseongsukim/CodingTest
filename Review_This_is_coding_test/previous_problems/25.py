
def solution(N, stages):
    num_person = len(stages)
    data = []
    stages.sort()
    for i in range(1, N + 1):
        count = stages.count(i)
        if num_person == 0:
            data.append((i, 0))
        else:
            data.append((i, count / num_person))
        num_person -= count
    data.sort(key= lambda x: x[1], reverse= True)
    answer = []
    for stage, rate in data:
        answer.append(stage)
    return answer


print(solution(5, [2, 1, 2, 6, 4, 3, 3]))
print(solution(4, [4, 4, 4, 4, 4]))