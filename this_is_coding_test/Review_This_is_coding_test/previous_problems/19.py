"""
6
1 2 3 4 5 6
2 1 1 1
=> 54 -24
"""
N = int(input())
numbers = list(map(int, input().split()))
plus, minus, multiply, divide = map(int, input().split())

def dfs(i, value, plus, minus, multiply, divide):
    global min_value, max_value
    if i == len(numbers):
        min_value = min(min_value, value)
        max_value = max(max_value, value)
    if plus > 0:
        dfs(i + 1, value + numbers[i], plus - 1, minus, multiply, divide)
    if minus > 0:
        dfs(i + 1, value - numbers[i], plus, minus - 1, multiply, divide)
    if multiply > 0:
        dfs(i + 1, value * numbers[i], plus, minus, multiply - 1, divide)
    if divide > 0:
        dfs(i + 1, int(value / numbers[i]), plus, minus, multiply, divide - 1)

min_value = 1e9
max_value = -1e9

dfs(1, numbers[0], plus, minus, multiply, divide)
print(max_value)
print(min_value)