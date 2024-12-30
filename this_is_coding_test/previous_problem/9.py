

def solution(s):
    total_length = len(s)
    if total_length == 1:
        return 1

    answer = total_length
    for i in range(1, total_length // 2 + 1):
        compressed = ""
        prev = s[0: i]
        count = 1
        for j in range(i, total_length, i):
            if prev == s[j: j + i]:
                count += 1
            else:
                compressed += str(count) + prev if count > 1 else prev
                prev = s[j: j + i]
                count = 1

        compressed += str(count) + prev if count > 1 else prev
        print(compressed)
        answer = min(answer, len(compressed))
    return answer





print(solution("aabbaccc")) # 7
# print(solution("ababcdcdababcdcd")) # 9
# print(solution("abcabcdede")) # 8
# print(solution("abcabcabcabcdedededede")) # 14
# print(solution("xababcdcdababcdcd")) # 17

