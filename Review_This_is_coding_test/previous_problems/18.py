
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
    return p[:count * 2], p[count * 2:]

def check(p):
    while True:
        length = len(p)
        p = p.replace("()","")
        if len(p) == length:
            break
    if p == "":
        return True
    else:
        return False

def solution(p):
    if p == '':
        return ''
    u, v = divide(p)
    if check(u):
        answer = u + solution(v)
    else:
        answer = "("
        answer += solution(v)
        answer += ")"
        new_u = []
        for i in u[1:-1]:
            if i == ")":
                new_u.append("(")
            else:
                new_u.append(")")
        answer += "".join(new_u)

    return answer

print(solution("(()())()"))
print(solution(")("))
print(solution("()))((()"))