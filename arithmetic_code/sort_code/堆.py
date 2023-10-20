import random


def sift_down(nums: list, n: int, i: int):
    while True:
        l = 2 * i + 1
        r = 2 * i + 2
        base = i
        if l < n and nums[l] > nums[base]:
            base = l
        if r < n and nums[r] > nums[base]:
            base = r
        if base == i:
            break
        nums[i], nums[base] = nums[base], nums[i]
        i = base


def heap_sort(nums):
    for i in range(len(nums)//2-1,-1,-1):
        sift_down(nums, len(nums), i)
    for i in range(len(nums) - 1, 0, -1):
        nums[0], nums[i] = nums[i], nums[0]
        sift_down(nums, i, 0)
    return nums


x = list(range(0, 10))
random.shuffle(x)
print(x)
print(heap_sort(x))
