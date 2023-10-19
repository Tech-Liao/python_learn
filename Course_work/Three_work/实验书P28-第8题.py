sum=0
for i in range(1,100,2):
   mpl=1
   for j in range(i,i+3):
      mpl *=j
   sum +=mpl
print(sum)
