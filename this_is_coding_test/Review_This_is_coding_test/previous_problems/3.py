numbers = input()
zero_count = 0
one_count = 0
first = numbers[0]
if first == "0":
    zero_count += 1
else:
    one_count += 1
for i in range(1, len(numbers) - 1):
    if numbers[i + 1] != numbers[i]:
        if numbers[i] == "0":
            zero_count += 1
        else:
            one_count += 1
print(min(zero_count, one_count))