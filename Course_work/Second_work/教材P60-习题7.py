n = int(input("请输入n："))
S = 1
for i in range(1,n):
    S =S+(-1)**(i+1)*(1/(2*i+1))
print("{:8f}".format(S))