from bisect import bisect_left, bisect_right
N, x = map(int, input().split())
arr = list(map(int, input().split()))

def count_by_range(arr, left_value, right_value):
    left_index = bisect_left(arr, left_value)
    right_index = bisect_right(arr, right_value)
    return right_index - left_index

if count_by_range(arr, x, x) == 0:
    print(-1)
else:
    print(count_by_range(arr, x, x))