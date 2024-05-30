"""
K1KA5CB7

AJKDLSI412K4JSJ9D
"""
inputs = input()

alphabets = []
numbers = []
for i in inputs:
    if i.isdigit():
        numbers.append(int(i))
    else:
        alphabets.append(i)

alphabets.sort()
sum_number = sum(numbers)

answer = ''
for alphabet in alphabets:
    answer += alphabet

print(answer + str(sum_number))