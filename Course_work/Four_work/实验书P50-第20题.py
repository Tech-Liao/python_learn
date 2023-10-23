dic_addree={}
while True:
    print("a.新增联系人")
    print("b.查询联系人")
    print("c.删除联系人")
    print("d.退出程序")
    ch=input("input a/b/c/d:")
    if ch=='a':
        name=input("input name:")
        if name in dic_addree:
            print("联系人已存在")
        else:
            numbers=input("input {}'telphone number:".format(name))
            dic_addree[name]=numbers
        continue
    elif ch=='b':
        name=input("input name:")
        if name in dic_addree:
            print("{} phone number:{}".format(name,dic_addree[name]))
        else:
            print("该人不在通讯录上")
        continue
    elif ch=='c':
        name=input("input name:")
        if name in dic_addree:
            del dic_addree[name]
            print("已删除")
        else:
            print("此人已不再通讯录")
        continue
    elif ch=='d':
        break
    else:
        print("输入错误")
