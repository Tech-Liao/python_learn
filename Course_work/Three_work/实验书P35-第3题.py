nums=[1,1]
for i in range(2,31):
   nums.append(nums[i-1]+nums[i-2])

for i in range(1,len(nums)+1):
   print(nums[i-1],end=' ')
   if i%5==0:
      print() 
