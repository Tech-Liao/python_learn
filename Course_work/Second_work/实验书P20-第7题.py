str1=input("请输入币值，美元以$结尾，人民币以￥结尾:")
n=float(str1[:-1])
flag=str1[-1]

if flag=='$':
   print("{}美元可以兑换人民币{}".format(n,n*6,868))
else:
   print("{}人民币可以兑换{}美元".format(n,n*0.1456))
