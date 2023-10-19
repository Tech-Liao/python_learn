lst_info=[ ["李玉","男",25], ["刘妍","女",21],["莫心","女",24],["沈冲","男",28]]
lst_del=[]
while True:
   str1=input("输入需要删除的员工姓名:")
   if str1 =='0':
      break
   for i in lst_info:
       if str1 in i:
          lst_del=i
          break
   else:
      print("无该员工")
      continue
   del lst_info[lst_info.index(lst_del)]
print(lst_info)
