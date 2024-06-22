"""
주식가격

"""
def solution(prices):
    answer = []
    for i in range(len(prices)):
        time = 0
        for j in range(i + 1, len(prices)):
            time += 1
            if prices[i] > prices[j]:
                break
        answer.append(time)
    return answer


print(solution([1, 2, 3, 2, 3])) # [4, 3, 1, 1, 0]
print(solution([2, 4, 3, 5, 2])) # [4, 1, 2, 1, 0]