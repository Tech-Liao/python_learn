n = int(input("请输入n："))
count = 0
for i in range(1,n+1):
    if i % 17 ==0 and i>count:
        count = i
print(count)
