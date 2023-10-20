import random

random.seed()
a = random.randrange(1, 100)
random.seed()
b = random.randrange(1, 100)
random.seed()
c = random.randrange(1, 100)
print(a, b, c)
for i in range(min(a, b, c), 1, -1):
    if a % i == 0 and b % i == 0 and c % i == 0:
        print("{},{},{}的最大公约数：{}".format(a, b, c, i))
        break
else:
    print("无最大公约数")
for i in range(2, min(a, b, c) + 1):
    if a % i == 0 and b % i == 0 and c % i == 0:
        print("{},{},{}的最小公倍数：{}".format(a, b, c, i))
        break