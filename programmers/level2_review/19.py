"""
괄호 회전하기
"""

def turn_left(s):
    new_s = ""
    for i in range(1, len(s)):
        new_s += s[i]
    new_s += s[0]
    return new_s

def solution(s):
    length = len(s)
    answer = 0
    for i in range(length):
        s = turn_left(s)
        candidate = s
        while True:
            l = len(candidate)
            candidate = candidate.replace("()", "")
            candidate = candidate.replace("{}", "")
            candidate = candidate.replace("[]", "")
            if l == len(candidate):
                break
        if len(candidate) == 0:
            answer += 1
    return answer




print(solution("[](){}")) # 3
print(solution("}]()[{")) # 2
print(solution("[)(]")) # 0
print(solution("}}}")) # 0
