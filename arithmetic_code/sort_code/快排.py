import random

def partition(low, height, nums):
    i = low
    j = height
    ra = random.randrange(low,height)
    nums[low],nums[ra]=nums[ra],nums[low]
    while i < j:

        while i < j and nums[i] <= nums[low]:
            i += 1
        while i < j and nums[j] >= nums[low]:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]
    nums[low], nums[i] = nums[i], nums[low]
    return i


def qsort(low, height, nums):
    while low < height:
        i = partition(low, height, nums)
        if i-low < height - i:
            qsort(low, i - 1, nums)
            low = i+1
        else:
            qsort(i + 1, height, nums)
            height = i-1


x = list(range(0, 20))
random.shuffle(x)
print(x)

qsort(0,len(x)-1, x)
print(x)

