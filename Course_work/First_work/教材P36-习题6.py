x = int(input("请输入一个三位整数："))
sum = 0
for i in range(3):
    sum += (x%10)
    x = x//10
print(sum)
