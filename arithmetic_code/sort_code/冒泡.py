import random
x=list(range(0,20))
random.shuffle(x)
print(x)
for i in range(20):
    for j in range(20-i-1):
        if x[j] < x[j+1]:
            x[j],x[j+1] = x[j+1],x[j]

print(x)
