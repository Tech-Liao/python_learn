import random

nums=[]
for i in range(20):
   nums.append(random.randrange(10,100))
nums[0:11]=sorted(nums[0:11])
nums[11:]=sorted(nums[11:],reverse=True)
print(nums)
