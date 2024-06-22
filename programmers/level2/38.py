"""
뒤에 있는 큰 수 찾기

"""
def solution(numbers):
    answer = [-1] * len(numbers)
    stack = [0]
    for i in range(1, len(numbers)):
        target = numbers[i]
        while stack and numbers[stack[-1]] < target:
            answer[stack.pop()] = target
        stack.append(i)
    return answer

def another_solution(numbers):
    answer = [-1] * len(numbers)
    stack = []
    for i in range(len(numbers) - 1, -1, -1):
        while stack and numbers[i] >= stack[-1]:
            stack.pop()
        if stack:
            answer[i] = stack[-1]
        stack.append(numbers[i])
    return answer


print(solution([2, 3, 3, 5])) # [3, 5, 5, -1]
print(solution([9, 1, 5, 3, 6, 2])) # [-1, 5, 6, 6, -1, -1]
print(solution([9, 1, 2, 5, 3, 4, 6, 2])) # [-1, 2, 5, 6, 4, 6, -1, -1]


print(another_solution([2, 3, 3, 5])) # [3, 5, 5, -1]
print(another_solution([9, 1, 5, 3, 6, 2])) # [-1, 5, 6, 6, -1, -1]
print(another_solution([9, 1, 2, 5, 3, 4, 6, 2])) # [-1, 2, 5, 6, 4, 6, -1, -1]
