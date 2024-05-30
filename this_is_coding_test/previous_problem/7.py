"""
123402

7755
"""
import sys
input = sys.stdin.readline
skill = input()

length = len(skill)
index = length // 2
left = skill[:index]
right = skill[index:]

left_sum = 0
right_sum = 0
for l, r in zip(left, right):
    left_sum += int(l)
    right_sum += int(r)

if left_sum == right_sum:
    print('LUCKY')
else:
    print('READY')
