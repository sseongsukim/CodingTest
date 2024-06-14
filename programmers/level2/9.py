"""
Note that how to use stack
"""
def solution(s):
    stack = []
    for element in s:
        stack.append(element)
        if len(stack) > 1 and stack[-1] == stack[-2]:
            stack.pop()
            stack.pop()
    return 1 if stack == [] else 0

print(solution("baabaa")) # 1
print(solution("cdcd")) # 0