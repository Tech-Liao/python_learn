import sys

for line in sys.stdin:
    a=line.split()
m=int(a[0])
n=int(a[1])
prod1=1
prod2=1
prod3=1
for i in range(1,m+1):
    prod1*=i

for i in range(1,n+1):
    prod2*=i
for i in range(1,m-n+1):
    prod3*=i
print(prod1//(prod2*prod3))
