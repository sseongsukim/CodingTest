"""
요격 시스템
"""
def solution(targets):
    answer = 0
    shoot = 0
    targets.sort(key= lambda x: (x[1]))
    for target in targets:
        if target[0] > shoot:
            answer += 1
            shoot = target[1] - 0.5

    return answer

print(solution([[4,5],[4,8],[10,14],[11,13],[5,12],[3,7],[1,4]])) # 3
