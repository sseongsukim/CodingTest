"""
5
8 3 7 9 2
3
5 7 9
"""
N = int(input())
numbers = sorted(list(map(int, input().split())))
M = int(input())
requests = list(map(int, input().split()))

def binary_search(arr, start, target, end):
    if start > end:
        return None
    mid = (start + end) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search(arr, mid + 1, target, end)
    else:
        return binary_search(arr, start, target, mid - 1)

for r in requests:
    answer = binary_search(numbers, 0, r, N - 1)
    if answer is None:
        print("no", end= ' ')
    else:
        print("yes", end= ' ')