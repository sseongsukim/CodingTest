"""
Note that stack is much faster than replace !
"""
def solution(s):
    if s[0] == ")" or s[-1] == "(":
        return False
    count = 1
    stack = []
    for element in s[1:]:
        if element == "(":
            count += 1
        else:
            stack.append(element)
        if count < len(stack):
            return False
    if len(stack) != count:
        return False
    else:
        return True

print(solution("()()")) # True
print(solution("(())()")) # True
print(solution(")()(")) # False
print(solution("(()(")) # False
print(solution("()))()((()")) # False