lst_floor=[1,4,2,5,7,3]

for i in range(1,len(lst_floor)):
   count=lst_floor[i]-lst_floor[i-1]
   if count>0:
      for i in range(count):
          print("↑",end=' ')
   else:
      for i in range(-count):
          print("↓",end=' ')

print()
