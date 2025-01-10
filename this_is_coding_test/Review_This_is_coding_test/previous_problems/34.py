N = int(input())
numbers = list(map(int, input().split()))

numbers.reverse()

d = [1] * N
for i in range(1, N):
    for j in range(i):
        if numbers[j] < numbers[i]:
            d[i] = max(d[i], d[j] + 1)
print(N - max(d))