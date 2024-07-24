"""
짝지어 제거하기
"""
def solution(s):
    stack = []
    for element in s:
        stack.append(element)
        if len(stack) > 1 and stack[-2] == stack[-1]:
            stack.pop()
            stack.pop()
    if len(stack) == 0:
        return 1
    else:
        return 0


print(solution("baabaa")) # 1
print(solution("cdcd")) # 0