import sys
arr = []
for line in sys.stdin:
    temp = list(line[:-1])
    arr.append(temp)
len1 = len(arr[0]) - 1
len2 = len(arr[1]) - 1

count = 0
flag = 0
while len1 >=0 and len2 >=0:
    a, b = int(arr[0][len1]), int(arr[1][len2])
    if a + b + flag >= 10:
        flag = (a + b + flag) // 10
        count += 1
    else:
        flag = 0
    len1 -= 1
    len2 -= 1
while len1 >=0:
    a = int(arr[0][len1])
    if a + flag >= 10:
        flag = (a + flag) // 10
        count += 1
    else:
        flag = 0
    len1 -= 1
while len2 >=0:
    b = int(arr[1][len2])
    if b + flag >= 10:
        flag = (b + flag) // 10
        count += 1
    else:
        flag = 0
    len2 -= 1
print(count)

