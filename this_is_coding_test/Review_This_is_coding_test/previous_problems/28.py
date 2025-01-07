"""
7
-15 -4 2 8 9 13 15

5
-15 -6 1 3 7
"""
N = int(input())
numbers = list(map(int, input().split()))

def binary_search(array, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if array[mid] == mid:
        return mid
    elif array[mid] < mid:
        return binary_search(array, mid + 1, end)
    else:
        return binary_search(array, start, mid - 1)

answer = binary_search(numbers, 0, N - 1)
if answer is None:
    print(-1)
else:
    print(answer)