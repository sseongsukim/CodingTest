"""
10 7
1 3 5 7 9 11 13 15 17 19
"""
N, T = map(int, input().split())
arr = list(map(int, input().split()))

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


answer = binary_search(arr, 0, T, N - 1)
if answer is None:
    print('No')
else:
    print(answer)
