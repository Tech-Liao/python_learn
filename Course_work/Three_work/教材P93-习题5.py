import random
l=[]
for i in range(20):
   l.append(random.randrange(1000,5001))
for i in l:
    if i%2!=0 and i%3!=0 and i%5!=0  and i%7!=0:
       print(i,end=' ')

print()
