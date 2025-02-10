N = int(input())
numbers = list(map(int, input().split()))
numbers.sort()

target = 1
for num in numbers:
    if num > target:
        break
    else:
        target += num
        
print(target)