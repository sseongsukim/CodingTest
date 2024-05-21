
def divide(p):
    first = p[0]
    stack = []
    count = 1
    for i in p[1:]:
        if i == first:
            count += 1
        else:
            stack.append(i)

        if count == len(stack):
            break
    u = p[:count * 2]
    v = p[count * 2:]
    return u, v

def check(p):
    while True:
        length = len(p)
        p = p.replace("()", "")
        if len(p) == length:
            break

    if p == "":
        return True
    else:
        return False

def solution(p):
    if p == "":
        return ""
    answer = ""
    u, v = divide(p)
    if check(u):
        answer = u + solution(v)
    else:
        answer = "("
        answer += solution(v)
        answer += ")"
        for i in list(u[1: -1]):
            if i == "(":
                answer += ")"
            else:
                answer += "("

    return answer

print(solution(")("))
print(solution("(()())()"))
print(solution("()))((()"))