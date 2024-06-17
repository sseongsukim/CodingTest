"""
기능개발

"""

def solution(progresses, speeds):
    for i in range(len(progresses)):
        progresses[i] = 100 - progresses[i]

    answer = []
    while len(progresses) >= 1:
        if progresses[0] % speeds[0] == 0:
            numbers = progresses[0] // speeds[0]
        else:
            numbers = (progresses[0] // speeds[0]) + 1

        for i in range(len(progresses)):
            progresses[i] -= (speeds[i] * numbers)

        index = 0
        for i in range(len(progresses)):
            if progresses[i] > 0:
                index = i
                break
        if index == 0:
            answer.append(len(progresses))
            break
        else:
            progresses = progresses[index:]
            speeds = speeds[index:]
            answer.append(index)
    return answer




print(solution([93, 30, 55], [1, 30, 5])) # [2, 1]
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1])) # [1, 3, 2]