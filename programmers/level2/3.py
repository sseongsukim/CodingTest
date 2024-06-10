
def solution(A, B):
    A.sort()
    B.sort(reverse= True)
    answer = []
    for a, b in zip(A, B):
        answer.append(a * b)
    return sum(answer)

print(solution([1, 4, 2], [5, 4, 4])) # 29
print(solution([1, 2], [3, 4])) # 10