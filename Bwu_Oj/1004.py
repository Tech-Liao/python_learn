import sys
import math

for line in sys.stdin:
    a=line.split()
m=int(a[0])
n=int(a[1])
sum=0
for i in range(m,n+1):
    for j in range(2,i):
        if i%j == 0:
            break
    else:
        if i == 1:
            continue
        else:
            sum += i
print(sum)

