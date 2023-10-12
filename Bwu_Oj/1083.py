import sys

for line in sys.stdin:
    arr=line[:-1]
l=len(arr)-1
while l>0:
    print(arr[l],end='')
    l-=1
print()
