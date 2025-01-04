
def solution(N, stages):
    answer = []
    total_people = len(stages)
    stages.sort()
    for i in range(1, N + 1):
        current_stage_people = stages.count(i)
        if total_people == 0:
            answer.append((0, i))
        else:
            answer.append((current_stage_people / total_people, i))
            total_people -= current_stage_people

    answer.sort(key= lambda x: -x[0])
    result = []

    for rate, stage in answer:
        result.append(stage)
    return result

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3])) # [3, 4, 2, 1, 5]
print(solution(4, [4, 4, 4, 4, 4])) # [4, 1, 2, 3]