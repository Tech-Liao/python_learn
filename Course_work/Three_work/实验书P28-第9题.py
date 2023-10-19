s=input("enter two num:")
l=s.split(' ')
a=int(l[0])
n=int(l[1])
i=0
sums=0
while i<n:
   nums=0
   for j in range(i+1):
      nums = nums*10+a
   sums += nums
   i+=1
print(sums)
