"""
5
-15 -6 1 3 7

7
-15 -4 2 8 9 13 15

7
-15 -4 3 8 9 13 15
"""
N = int(input())
arr = list(map(int, input().split()))

def binary_search(arr, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if arr[mid] == mid:
        return mid
    elif arr[mid] < mid:
        return binary_search(arr, mid + 1, end)
    else:
        return binary_search(arr, start, mid - 1)

if binary_search(arr, 0, N - 1) is None:
    print(-1)
else:
    print(binary_search(arr, 0, N - 1))
