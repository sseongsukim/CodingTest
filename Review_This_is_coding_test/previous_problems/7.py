"""
123402
-> LUCKY
7755
-> READY
"""
N = input()
length = len(N)
left = N[: length// 2]
right = N[length // 2:]

left_value = 0
right_value = 0

for l, r in zip(left, right):
    left_value += int(l)
    right_value += int(r)

if left_value == right_value:
    print("LUCKY")
else:
    print("READY")