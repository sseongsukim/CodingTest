"""
거스름돈
"""
N = 1260
arr = [500, 100, 50, 10]

count = 0
for a in arr:
    count += N // a
    N %= a

print(count)