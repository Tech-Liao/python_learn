import math
import sys
a=int(input("请输入三角形第一条边a:"))
b=int(input("请输入三角形第一条边b:"))
c=int(input("请输入三角形第一条边c:"))
if a>b:
    a,b=b,a
if a>c:
    a,c=c,a
if b>c:
    b,c=c,b
if a+b<c:
    print("三角形不成立")
    exit()

l=(a+b+c)/2
area=math.sqrt(l*(l-a)*(l-b)*(l-c))
print("该三角形的面积为：{:.3f}".format(area))
