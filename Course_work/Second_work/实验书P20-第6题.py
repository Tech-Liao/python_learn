str1=input("请输入要兑换的美元币值:")
n=float(str1[:-1])
print("{}美元可以兑换人民币{:.2f}".format(n,n*6.868))
