month=[31,28,31,30,31,30,31,31,30,31,30,31]
while True:
   n=int(input("enter a num:"))
   if n==0:
      break
   print(month[n-1])
