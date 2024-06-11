"""
Note that how to use stack
"""
def solution(s):
    stack = []
    for i in range(len(s)):
        stack.append(s[i])
        if len(stack) >= 2 and stack[-1] == stack[-2]:
            stack.pop()
            stack.pop()
    return 1 if stack == [] else 0

print(solution("baabaa")) # 1
print(solution("cdcd")) # 0