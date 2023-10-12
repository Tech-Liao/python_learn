import sys


def x_num(ele):
    x = 0
    l_ele = len(ele)
    for i in range(l_ele - 1, -1, -1):
        x = x * 10 + ele[i]
    return x


def func(num):
    element = []
    if num == 0:
        element = [0]
        return element
    while num > 0:
        element.append(num % 10)
        num //= 10

    return element


def Lucky_num(x, y):
    while True:
        ele = func(x)
        ele_sum = sum(ele)
        l_ele = len(ele)
        if ele_sum == y:
            return x
        if y < ele[l_ele - 1]:
            return -1
        elif y == ele[l_ele - 1]:
            for i in range(l_ele - 1):
                if ele[i] != 0:
                    return -1
        x = x + 1


arr = []
for line in sys.stdin:
    arr.append(line.split())
print(arr)
for i in range(len(arr)):
    x = int(arr[i][0])
    y = int(arr[i][1])
    n = y // 9
    Max = 0
    if y > 9000:
        print(-1)
        break
    else:
        for i in range(n):
            Max += 9 * 10 ** i
        if y % 9 == 0:
            if Max > x:
                print(Max)
                break
            else:
                x = Lucky_num(x, y)
                print(x)
                break
        else:
            Max = Max + 1
            if Max > x:
                x = Max
            x = Lucky_num(x, y)
            print(x)
            break

