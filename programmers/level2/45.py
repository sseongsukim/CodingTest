"""
스킬트리

"""
def solution(skill, skill_trees):
    answer = 0
    for skills in skill_trees:
        indices = []
        for s in skills:
            if s in skill:
                indices.append(skill.index(s))
        is_true = True
        for i in range(len(indices)):
            if i != indices[i]:
                is_true = False
                break
        if is_true:
            answer += 1
    return answer


print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"])) # 2