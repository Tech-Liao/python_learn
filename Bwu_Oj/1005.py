import sys
import math

for line in sys.stdin:
    a=line.split()
theta=float(a[0])
print(math.sin(theta)+math.cos(theta))
