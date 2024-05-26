"""
02984
567
"""
numbers = input()
answer = int(numbers[0])
for i in range(1, len(numbers)):
    if answer <= 1 or numbers[i] == "0":
        answer += int(numbers[i])
    else:
        answer *= int(numbers[i])

print(answer)