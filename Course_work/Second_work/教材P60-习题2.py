while True:
    x = int(input("请输入一个正整数："))
    if x>100 or x<0:
        print("成绩有误")
        break
    elif x>=90:
        print('A')
    elif 80<=x<89:
        print('B')
    elif 70<=x<79:
        print('B')
    elif 60<=x<69:
        print('D')
    else:
        print('E')