"""
튜플

"""
def solution(s):
    answer = {}
    s = s[1: -1]
    components = s.split(",")
    stack = []
    for component in components:
        if component[0] == "{" and component[-1] == "}":
            answer[1] = int(component[1: -1])
        if component[0] != "{" and component[-1] != "}":
            stack.append(int(component))
        if component[0] == "{" and component[-1] != "}":
            stack.append(int(component[1:]))
        if component[-1] == "}" and component[0] != "{":
            stack.append(int(component[:-1]))
            answer[len(stack)] = stack
            stack = []
    result = [answer[1]]

    for key in sorted(answer.keys())[1:]:
        for r in result:
            answer[key].remove(r)
        result.append(answer[key][0])
    return result

print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}")) # [2, 1, 3, 4]
print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}")) # [2, 1, 3, 4]
print(solution("{{20,111},{111}}")) # [111, 20]
print(solution("{{123}}")) # [123]
print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}")) # [3, 2, 4, 1]