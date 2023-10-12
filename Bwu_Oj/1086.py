import sys

def cm(x):
    res=1
    while x>0:
        res *=x
        x-=1
    return res

def func(per):
    res=1
    n=1
    i=1
    while i>per:
        res+=i
        n+=1
        i = 1/cm(n)
    return res
         


for line in sys.stdin:
    arr=line.split()
per=float(arr[0])
res=func(per)
print("e={:.10f}".format(res))
