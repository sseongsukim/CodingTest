
def solution(s):
    total_length = len(s)
    if total_length == 1:
        return 1

    answer = total_length
    for i in range(1, total_length // 2 + 1):
        compress = ""
        prev = s[:i]
        count = 1
        for j in range(i, total_length, i):
            if prev == s[j:j+i]:
                count += 1
            else:
                compress += str(count) + prev if count > 1 else prev
                count = 1
                prev = s[j:j+i]
        compress += str(count) + prev if count > 1 else prev
        answer = min(answer, len(compress))
    return answer

print(solution("aabbaccc"))
print(solution("ababcdcdababcdcd"))
print(solution("abcabcdede"))