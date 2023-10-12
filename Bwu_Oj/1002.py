import sys

count=0
for line in sys.stdin:
    for ch in line:
        if ch =='$':
            count+=1
print(count)
