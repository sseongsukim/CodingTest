inputs = input()

alphabets = []
numbers = 0

for i in inputs:
    if i.isdigit():
        numbers += int(i)
    else:
        alphabets.append(i)

alphabets.sort()
answer = ""
for a in alphabets:
    answer += a
answer += str(numbers)
print(answer)