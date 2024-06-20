"""
[3차] 압축
int to alphabet = chr(int_value + 65)
"""
def solution(msg):
    alphabet_dict = {}
    for i in range(0, 26):
        alpha = chr(i + 65)
        alphabet_dict[alpha] = i + 1

    answer = [0]
    value = 26
    current_word = ""
    for i in range(len(msg)):
        current_word += msg[i]
        if current_word not in alphabet_dict.keys():
            value += 1
            alphabet_dict[current_word] = value
            current_word = msg[i]
            answer.append(alphabet_dict[current_word])
        else:
            answer[-1] = alphabet_dict[current_word]
    return answer


print(solution("KAKAO")) # [11, 1, 27, 15]
# print(solution("TOBEORNOTTOBEORTOBEORNOT")) # [20, 15, 2, 5, 15, 18, 14, 15, 20, 27, 29, 31, 36, 30, 32, 34]
# print(solution("ABABABABABABABAB")) # [1, 2, 27, 29, 28, 31, 30]