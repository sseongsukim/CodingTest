"""
5
-15 -6 1 3 7

7
-15 -4 2 8 9 13 15

7
-15 -4 3 8 9 13 15
"""
N = int(input())
numbers = list(map(int, input().split()))

def binary_search(numbers, start, end):
    mid = (start + end) // 2
    while start <= end:
        if numbers[mid] == mid:
            return mid
        elif numbers[mid] < mid:
            return binary_search(numbers, mid + 1, end)
        else:
            return binary_search(numbers, start, mid - 1)

print(binary_search(numbers, 0, len(numbers) - 1))
