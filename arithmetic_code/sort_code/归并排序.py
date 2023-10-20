import random

def merge_sort(x, l, r):
    if l >= r:
        return
    mid = (l + r) // 2
    # 划分
    merge_sort(x, l, mid)
    merge_sort(x, mid + 1, r)
    # 合并
    temp = x[l:r + 1]
    i = 0
    j = mid - l + 1
    for k in range(l, r + 1):
        if i == mid - l + 1:
            x[k] = temp[j]
            j += 1
        elif j == r - l + 1 or temp[i] <= temp[j]:
            x[k] = temp[i]
            i += 1
        else:
            x[k] = temp[j]
            j += 1


x = list(range(0, 20))
random.shuffle(x)
print(x)

merge_sort(x, 0, 19)
print(x)
