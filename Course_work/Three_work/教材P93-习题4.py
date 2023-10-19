s=input("enter an english string:")
l=s.split(" ")
Max=0
flag=0
for i in l:
    if len(i)>Max:
       Max=len(i)
       flag=i
print(flag)
