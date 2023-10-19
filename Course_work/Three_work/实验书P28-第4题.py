count=0
for i in range(1000,2001):
   if i %400==0 or (i %4==0 and i%100!=0):
      count +=1
      print(i,end=' ')
      if count%5==0:
         print()
print()
