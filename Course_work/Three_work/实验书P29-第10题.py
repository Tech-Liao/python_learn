import random

n=random.randrange(0,9)
random.seed(n)
n=random.randrange(0,10)
count=0
while True:
   x=int(input("enter a num:"))
   if x> n:
      print("big")
      count+=1
   elif x<n:
      print("small")
      count+=1
   else:
      print("{}次，猜对!".format(count))
      break


