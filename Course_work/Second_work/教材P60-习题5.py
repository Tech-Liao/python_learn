import math

n = int(input("请输入n："))
for i in range(1, n + 1):
    y = 1.0
    while abs(y * y - i) > 1e-8:
        y = (y + i / y) / 2
    print(y, math.sqrt(i))
