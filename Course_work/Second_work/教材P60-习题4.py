import math
for i in range(0,90+1,5):
    r = math.radians(i)
    print("sin({:.2f}):{:.2f},cos({:.2f}):{:.2f}".format(r,math.sin(r),r,math.cos(r)))