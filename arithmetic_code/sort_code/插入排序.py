import random
def insert_sort(nums:list):
    n = len(nums)
    for i in range(1,n):
        base = nums[i]
        j = i-1
        while j>=0 and nums[j]>base:
            nums[j+1] = nums[j]
            j -=1
        nums[j+1]=base
    return nums


x = list(range(0, 20))
random.shuffle(x)
print(x)
print(insert_sort(x))
