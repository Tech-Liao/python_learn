l=float(input("请输入行程的总里程:"))
if abs(l-0.0)<10e-5:
   print("里程数输入错误")
elif l<=3:
   print("需要支付10元")
elif 3<l<=10:
   print("需要支付{:.1f}元".format(10+(l-3)*1.2))
else:
   print("需要支付{:.1f}元".format(18.4+(l-10)*1.5))
