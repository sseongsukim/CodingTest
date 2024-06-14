"""
괄호 회전하기

"""
import copy

def turn_left(s):
    new_s = ""
    for i in range(1, len(s)):
        new_s += s[i]
    new_s += s[0]
    return new_s

def solution(s):
    answer = 0
    turning_time = len(s)
    for _ in range(turning_time):
        s = turn_left(s)
        new_s = copy.deepcopy(s)
        while True:
            length = len(new_s)
            new_s = new_s.replace("()", "")
            new_s = new_s.replace("[]", "")
            new_s = new_s.replace("{}", "")
            if length == len(new_s):
                break
        if len(new_s) == 0:
            answer += 1
    return answer

print(solution("[](){}")) # 3
print(solution("}]()[{")) # 2
print(solution("[)(]")) # 0
print(solution("}}}")) # 0

