s = input()

answer = int(s[0])
for i in range(1, len(s)):
    if answer <= 1 or int(s[i]) <= 1:
        answer += int(s[i])
    else:
        answer *= int(s[i])
print(answer)