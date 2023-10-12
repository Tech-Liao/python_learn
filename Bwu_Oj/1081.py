import sys


def find_numbers(a, b, n, m):
    numbers = []
    for _ in range(m):
        # 找到第一个不小于n的a的倍数
        while n <= a:
            n += a
        numbers.append(n)
        # 找到第一个不大于n且不小于n+b的b的倍数
        while n < n + b:
            n += b
        n += b  # 跳过已经取过的数
    return numbers


for line in sys.stdin:
    arr = line.split()
a, b, n, m = int(arr[0]), int(arr[1]), int(arr[2]), int(arr[3])
if a >= 1 and b >= 1 and n >= 1 and m >= 1:
    res=find_numbers(a,b,n,m)
    print(res)
else:
    print("Invalid Arguments")
