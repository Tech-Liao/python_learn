x=1
for i in range(1,366,7):
   for j in range(0,5):
      x *=1.01
   for k in range(0,2):
      x *=0.99

print("{:.2f}".format(x))
