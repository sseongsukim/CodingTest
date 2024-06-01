"""
2
5 6
0 0 1 0
-> 30 30
3
3 4 5
1 0 1 0
-> 35 17
6
1 2 3 4 5 6
2 1 1 1
-> 54 -24
"""
N = int(input())
numbers = list(map(int, input().split()))
plus, minus, multiply, divide = map(int, input().split())

max_value = -int(1e9)
min_value = int(1e9)
def dfs(i, total, plus, minus, multiply, divide):
    global max_value, min_value
    if i == N:
        max_value = max(max_value, total)
        min_value = min(min_value, total)
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