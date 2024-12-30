
def solution(s):
    if len(s) == 1:
        return 1

    total_length = len(s)
    answer = total_length
    for i in range(1, total_length // 2 + 1):
        compress = ""
        prev = s[:i]
        count = 1
        for j in range(i, total_length, i):
            if prev == s[j:i+j]:
                count += 1
            else:
                compress += str(count) + prev if count > 1 else prev
                count = 1
                prev = s[j:i+j]
        compress += str(count) + prev if count > 1 else prev
        answer = min(answer, len(compress))
    return answer

print(solution("aabbacc"))



