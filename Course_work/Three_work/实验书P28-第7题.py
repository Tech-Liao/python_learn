sum_odd=0
sum_eve=0
while True:
   num=input("enter a num:")
   if num=='A':
      print(sum_odd,sum_eve)
      break
   num=int(num)
   if num%2!=0:
      sum_odd+=num
   else:
      sum_eve+=num

