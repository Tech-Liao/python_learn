import sys

count=0
arr=[]
for line in sys.stdin:
    temp=line.split()
    count+=len(temp)
    for i in range(len(temp)):
        arr.append(int(temp[i]))

arr_min=min(arr)
arr_max=max(arr)
print("Positive Number:{}".format(count))
print("Range:[{},{}]".format(arr_min,arr_max))
