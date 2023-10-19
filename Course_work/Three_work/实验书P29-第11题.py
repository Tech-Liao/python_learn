import random

n=random.randint(0,100)
m=random.randint(0,100)
print(m,n)
Min=min(m,n)
x=0
for i in range(m,0,-1):
    if m%i==0 and n%i==0:
       x=i
       print("最大公约数:{}".format(i))
       break

if m>n:
   if m%n==0:
      print(m)
   else:
      a=m//x
      b=n//x
      print(a*b*x)
else:
   if n%m==0:
      print(n)
   else:
      a=m//x
      b=n//x
      print(a*b*x)
      
