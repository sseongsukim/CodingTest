"""
마법의 엘리베이터

"""
def solution(storey):
    answer = 0
    storey = str(storey)
    while int(storey) != 0:
        length = len(storey)
        for i in range(length - 1, -1, -1):
            if int(storey[i]) != 0:
                index = i
                c = length - index - 1
                break
        int_stroey = int(storey)
        if int(storey[index]) > 5:
            answer += 10 - int(storey[index])
            int_stroey += (10 ** (c + 1)) - ((10 ** c) * int(storey[index]))
        elif int(storey[index]) < 5:
            answer += int(storey[index])
            int_stroey -= (10 ** c) * int(storey[index])
        else:
            if int(storey[index - 1]) >= 5:
                answer += 10 - int(storey[index])
                int_stroey += (10 ** (c + 1)) - ((10 ** c) * int(storey[index]))
            else:
                answer += int(storey[index])
                int_stroey -= (10 ** c) * int(storey[index])
        storey = str(int_stroey)
    return answer


print(solution(485)) # 1
print(solution(16)) # 6
print(solution(2554)) # 16
print(solution(6980)) # 6