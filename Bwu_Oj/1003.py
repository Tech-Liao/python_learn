import sys

for line in sys.stdin:
    a=line.split()
l=len(a)
arr_int=[]
for i in range(l):
    arr_int.append(int(a[i]))
sum=sum(arr_int)
avg=sum//l
count=0
for i in range(l):
    if arr_int[i]>avg:
        count+=1

print(count)
