def digits(num, exp):
    # 计算出第k位的数
    return (num // exp) % 10


def counting_sort_digit(nums, exp):
    counts = [0] * 10
    n = len(nums)
    for i in nums:
        d = digits(i, exp)
        counts[d] += 1
    for i in range(1, 10):
        counts[i] += counts[i - 1]
    res = [0] * n
    for i in range(n - 1, -1, -1):
        d = digits(nums[i], exp)
        j = counts[d] - 1
        res[j] = nums[i]
        counts[d] -= 1
    for i in range(n):
        nums[i] = res[i]


def radix_sort(nums):
    m = max(nums)
    exp = 1
    while exp <= m:
        counting_sort_digit(nums, exp)
        exp *= 10
    return nums
