import math
import sys
arr = []
for line in sys.stdin:
    temp = line.split()
    arr.append(temp)

arr_len = len(arr)
for i in range(arr_len):
    x1 = int(arr[i][0])
    y1 = int(arr[i][1])
    x2 = int(arr[i][2])
    y2 = int(arr[i][3])
    x3 = int(arr[i][4])
    y3 = int(arr[i][5])
    if x1 == 0 and x2 == 0 and x3 == 0 and y1 == 0 and y2 == 0 and y3 == 0:
        break
    if (x1 == x2 and y1 == y2) or (x1 == x3 and y1 == y3) or (x2 == x3 and y2 == y3):
        if (x1 == x2 and y1 == y2) and (x1 == x3 and y1 == y3):
            print("Not Colinear")
        else:
            print("Colinear")
        continue
    l1 = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    l2 = math.sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2)
    l3 = math.sqrt((x3 - x1) ** 2 + (y3 - y1) ** 2)
    a = x2 - x1
    b = y2 - y1
    a1 = x3 - x1
    b1 = y3 - y1
    theta = abs((a * a1 + b * b1) / (l1 * l3))
    if l1 > l2:
        l1, l2 = l2, l1
    if l1 > l3:
        l1, l3 = l3, l1
    if l2 > l3:
        l2, l3 = l3, l2
    if abs(l1 + l2 - l3) < 10e-6:
        if abs(theta - 1) < 10e-6:
            print("Colinear")
        else:
            print("Not Colinear")
    else:
        print("Not Colinear")

