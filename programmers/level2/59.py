"""
큰 수 만들기

"""
def solution(number, k):
    stack = []
    for num in number:
        while stack and stack[-1] < num and k > 0:
            stack.pop()
            k -= 1
        stack.append(num)
    return "".join(stack[:len(number) - k])



print(solution('1924', 2)) # '94'
print(solution('1231234', 3)) # '3234'
print(solution('4177252841', 4)) # '775841'