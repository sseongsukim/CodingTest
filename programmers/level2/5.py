"""
Make N to binary scale -> bin(N)
"""
def solution(s):
    answer = []
    zero_count = 0
    change_count = 0
    while s != "1":
        num_zero = s.count("0")
        s = s.replace("0", "")
        length = len(s)
        s = bin(length).split('b')[1]

        zero_count += num_zero
        change_count += 1

    answer.append(change_count)
    answer.append(zero_count)
    return answer

print(solution("110010101001"))
print(solution("01110"))
print(solution("1111111"))