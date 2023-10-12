import sys


def is_fibonacci(num):
    fib = [1, 1]
    while fib[-1] < num:
        fib.append(fib[-1] + fib[-2])
    l = len(fib) - 1
    sum = 0
    while l >= 0:
        if fib[l] == num:
            return True
        elif fib[l] > num:
            l -= 1
            continue
        else:
            sum += fib[l]
            l -= 1
        if sum == num:
            return True
        elif sum > num:
            sum = 0
            l += 1
    return False


arr = []
for line in sys.stdin:
    if line=="\n":
        break
    arr.append(line.strip())

for i in range(len(arr)):
    if is_fibonacci(int(arr[i])):
        print("Yes")
    else:
        print("No")
