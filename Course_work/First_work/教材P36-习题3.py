import math

x1 = eval(input("请输入第一个坐标的横坐标："))
y1 = eval(input("请输入第一个坐标的纵坐标："))

x2 = eval(input("请输入第二个坐标的横坐标："))
y2 = eval(input("请输入第二个坐标的纵坐标："))
x = x1 - x2
y = y1 - y2
print("两点间距离：" + "{:.2f}".format(math.sqrt(x ** 2 + y ** 2)))
