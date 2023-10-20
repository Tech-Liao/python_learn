for i in range(1,4+1):
    age = int(input("请输入年龄:"))
    experience = int(input("请输入工作经验："))
    major = input("请输入专业：")
    if age<25 and major == "计算机":
        print("获得面试机会")
    elif major == "电子" and experience>4:
        print("获得面试机会")
    elif major == "通信":
        print("获得面试机会")
    else:
        print("抱歉，您不符合面试要求")