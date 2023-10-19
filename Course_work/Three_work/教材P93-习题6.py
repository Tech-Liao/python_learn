data=[ ['王平','男',1,1,0,0],
       ['李丽','女',0,1,0,1],
       ['陈小梅','女',0,0,1,0],
       ['孙洪涛','男',0,1,1,1],
       ['方亮','男',1,0,1,0]]

compete=[]
name=[]
for i in data:
   compete.append(i[2:])
   name.append(i[:2])
count_two=0
count_3000=0
for i in compete:
   if sum(i)>=2:
      count_two+=1
   if i[1]==1:
      count_3000+=1
print(count_two)
count_name=0
for i in name:
   if i[1]=='女':
      count_name+=1
print(count_name)
print(count_3000)
