"""
5
8 3 7 9 2
3
5 7 9
"""

def binary_search(numbers, start, target, end):
    if start > end:
        return None

    while start <= end:
        mid = (start + end) // 2
        if numbers[mid] == target:
            return mid
        elif numbers[mid] < target:
            return binary_search(numbers, mid + 1, target, end)
        else:
            return binary_search(numbers, start, target, mid - 1)



N = int(input())
numbers = list(map(int, input().split()))
M = int(input())
finds = list(map(int, input().split()))

numbers.sort()

for f in finds:
    if binary_search(numbers, 0, f, len(numbers) - 1) is None:
        print("no")
    else:
        print('yes')
