N = int(input())
numbers = list(map(int, input().split()))
numbers.sort()

count = 0
answer = 0
for num in numbers:
    count += 1
    if num <= count:
        count = 0
        answer += 1
print(answer)