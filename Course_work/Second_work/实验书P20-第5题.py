str1=input("请输入要兑换的人民币币值，以￥结束:")
n=float(str1[:-1])
print("{}元人民币可以兑换{:.2f}美元".format(n,n*0.1456))
