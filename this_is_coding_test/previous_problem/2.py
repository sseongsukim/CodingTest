"""
02984
567
"""
numbers = input()
answer = int(numbers[0])

for n in numbers[1:]:

    if n == "0" or answer <= 0:
        answer += int(n)
    else:
        answer *= int(n)

print(answer)