
def solution(s):
    total_length = len(s)
    if total_length == 1:
        return s

    answer = total_length
    for length in range(1, len(s) // 2 + 1):
        compress = ''
        first = s[:length]
        count = 1
        for j in range(length, len(s), length):
            if first == s[j: j + length]:
                count += 1
            else:
                compress += str(count) + first if count >= 2 else first
                first = s[j: j + length]
                count = 1
        compress += str(count) + first if count > 2 else first
        answer = min(answer, len(compress))
    return answer

print(solution("aabbaccc"))
