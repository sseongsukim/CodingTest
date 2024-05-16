

def solution(N, stages):
    total_number = len(stages)
    stages.sort()
    failure_list = []
    for i in range(1, N + 1):
        count = stages.count(i)

        if total_number == 0:
            failure_list.append((0, i))
        else:
            failure_list.append((count / total_number, i))

        total_number -= count

    failure_list.sort(key= lambda x: x[0], reverse= True)
    answer = []
    for failure in failure_list:
        answer.append(failure[1])
    return answer


print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4, [4, 4, 4, 4, 4]))