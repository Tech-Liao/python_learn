def bucket_sort(nums):
    num_max = max(nums)
    num_min=min(nums)
    bucket_range = (num_max-num_min)//len(nums)
    buckets = [ [] for i in range(len(nums)+1)]
    for k in nums:
        buckets[(k-num_min)//bucket_range].append(k)

    nums.clear()
    for i in buckets:
        for j in sorted(i):
            nums.append(j)
    return nums

