N = int(input())
numbers = list(map(int, input().split()))
numbers.sort()

target = 1
for number in numbers:
    if target < number:
        break
    target += number
print(target)