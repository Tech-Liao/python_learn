n=int(input("请输入一个三位数:"))
sum=0
for i in range(3):
   sum=sum*10+n%10
   n //=10
print(sum)
