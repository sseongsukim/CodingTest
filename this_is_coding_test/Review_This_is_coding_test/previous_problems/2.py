numbers = list(input())

answer = int(numbers[0])
for number in numbers[1:]:
    if answer <= 1 or int(number) <= 1:
        answer += int(number)
    else:
        answer *= int(number)
print(answer)