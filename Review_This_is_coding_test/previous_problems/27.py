"""
7 2
1 1 2 2 2 2 3
-> 4
7 4
1 1 2 2 2 2 3
-> -1
"""
from bisect import bisect_left, bisect_right
N, K = map(int, input().split())
numbers = list(map(int, input().split()))

def count_by_range(numbers, left_value, right_value):
    left_index = bisect_left(numbers, left_value)
    right_index = bisect_right(numbers, right_value)
    return right_index - left_index

print(count_by_range(numbers, K, K))