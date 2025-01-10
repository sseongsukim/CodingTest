n = int(input())

i2 = i3 = i5 = 0
x2, x3, x5 = 2, 3, 5

d = [0] * n
d[0] = 1

for i in range(1, n):
    d[i] = min(x2, x3, x5)
    if d[i] == x2:
        i2 += 1
        x2 = 2 * d[i2]
    if d[i] == x3:
        i3 += 1
        x3 = 3 * d[i3]
    if d[i] == x5:
        i5 += 1
        x5 = 5 * d[i5]

print(d[n - 1])