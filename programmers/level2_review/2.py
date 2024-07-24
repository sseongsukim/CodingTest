"""
올바른 괄호
"""
def solution(s):
    if s[0] == ")":
        return False
    stack = []
    count = 0
    # (())
    for element in s:
        if element == "(":
            stack.append(element)
        else:
            count += 1

        if len(stack) < count:
            return False
        elif len(stack) == count:
            stack = []
            count = 0

    if len(stack) == 0:
        return True
    else:
        return False

print(solution("()()")) # True
print(solution("(())()")) # True
print(solution(")()(")) # False
print(solution("(()(")) # False