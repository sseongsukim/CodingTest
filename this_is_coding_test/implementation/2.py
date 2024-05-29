"""
a1
-> 2
"""
location = input()
alphabet_to_number = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 6,
    "g": 7,
    "h": 8,
}
x = int(location[1])
y = alphabet_to_number[location[0]]

moving = [
    [-2, 1], [-2, -1],
    [2, 1], [2, -1],
    [1, 2], [1, -2],
    [-1, 2], [-1, -2],
]

count = 0
for move in moving:
    nx = x + move[0]
    ny = y + move[1]
    if 1 <= nx <= 8 and 1 <= ny <= 8:
        count += 1

print(count)