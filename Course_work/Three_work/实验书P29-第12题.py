import random

count_1=0
count_0=0
for i in range(1000):
   n=random.randrange(0,2)
   if n==0:
      count_0+=1
   else:
      count_1+=1
print(count_0,count_1)

