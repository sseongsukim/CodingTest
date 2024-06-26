"""
2개 이하로 다른 비트

"""
def binary_to_ten(x):
    x = "".join(x)
    x = '0b' + x
    return int(x, 2)

def solution(numbers):
    answer = []
    for number in numbers:
        bin_number = list(bin(number).split("b")[1])

        if "0" not in bin_number:
            bin_number = ["0"] + bin_number
            bin_number[0], bin_number[1] = bin_number[1], bin_number[0]
        elif bin_number[-1] == "0":
            bin_number[-1] = "1"
        else:
            zero_index = -1e9
            for i in range(len(bin_number) - 1, -1, -1):
                if bin_number[i] == "0":
                    zero_index = max(zero_index, i)
            bin_number[zero_index] = "1"
            bin_number[zero_index + 1] = "0"

        answer.append(binary_to_ten(bin_number))
    return answer


print(solution([2, 7])) # [3, 11]
