years=int(input("请输入4位整数:"))
if years%400==0 or (years%4==0 and years%100 !=0):
   print("润年")
else:
   print("平年")
