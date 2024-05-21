"""
2
5 6
0 0 1 0

3
3 4 5
1 0 1 0

6
1 2 3 4 5 6
2 1 1 1
"""
N = int(input())
numbers = list(map(int, input().split()))
plus, minus, multiply, divide = map(int, input().split())

max_value = -1e9
min_value = 1e9

def dfs(i, total, plus, minus, multiply, divide):
    global min_value, max_value
    if i == N:
        max_value = max(total, max_value)
        min_value = min(total, min_value)

    if plus:
        dfs(i + 1, total + numbers[i], plus - 1, minus, multiply, divide)
    if minus:
        dfs(i + 1, total - numbers[i], plus, minus - 1, multiply, divide)
    if multiply:
        dfs(i + 1, total * numbers[i], plus, minus, multiply - 1, divide)
    if divide:
        dfs(i + 1, int(total / numbers[i]), plus, minus, multiply, divide - 1)

dfs(1, numbers[0], plus, minus, multiply, divide)
print(max_value)
print(min_value)