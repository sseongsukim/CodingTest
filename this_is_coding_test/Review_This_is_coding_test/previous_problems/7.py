numbers = input()

length = len(numbers)
left = numbers[:length // 2]
right = numbers[length // 2:]

left_sum = 0
right_sum = 0
for l, r in zip(left, right):
    left_sum += int(l)
    right_sum += int(r)
if left_sum == right_sum:
    print("LUCKY")
else:
    print("READY")