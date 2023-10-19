s=input("enter ten num:")
l=s.split(' ')
l=[int(i) for i in l]
print(l)
sum_odd=0
sum_eve=0
for i in l:
   if i%2!=0:
      sum_odd+=i
   else:
      sum_eve+=i
print(sum_odd,sum_eve)
