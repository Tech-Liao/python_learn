
fib=[1,1]
for i in range(2,20):
   fib_num=fib[i-1]+fib[i-2]
   fib.append(fib_num)
count=0
for i in fib:
   print(i,end=' ')
   count+=1
   if count%5==0:
      print()
print()
