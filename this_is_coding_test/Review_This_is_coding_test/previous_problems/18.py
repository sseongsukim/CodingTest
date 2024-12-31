def balance_strings(p):
    left = 0
    right = 0
    if p[0] == "(":
        left += 1
    else:
        right += 1
    for word in p[1:]:
        if word == "(":
            left += 1
        else:
            right += 1
        if left == right:
            break

    return p[:left + right], p[left + right:]


def correct_strings(p):
    if p[0] == ")":
        return False
    while True:
        length = len(p)
        p = p.replace("()", "")
        if len(p) == length:
            break
    if len(p) >= 1:
        return False
    else:
        return True

def solution(p):
    answer = ""
    if len(p) == 0:
        return answer

    u, v = balance_strings(p)
    if correct_strings(u):
        return u + solution(v)
    else:
        answer += "("
        answer += solution(v)
        answer += ")"
        new_u = u[1:-1]
        for i in range(len(new_u)):
            if new_u[i] == "(":
                answer += ")"
            else:
                answer += "("
        return answer

print(solution("(()())()"))
print(solution(")("))
print(solution("()))((()"))