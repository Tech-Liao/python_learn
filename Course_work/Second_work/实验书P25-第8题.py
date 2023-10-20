x=float(input("请输入x:"))
y=float(input("请输入y:"))

if x>0:
   if y>0:
      print(1)
   elif y<0:
      print(4)
   else:
      print("在x轴上")
elif x<0:
   if y>0:
      print(2)
   elif y<0:
      print(3)
   else:
      print("在x轴上")
else:
   print("在y轴上")
