N = int(input())
numbers = list(map(int, input().split()))
numbers.sort()

team = 0
count = 0
for number in numbers:
    count += 1
    if count >= number:
        count = 0
        team += 1
print(team)