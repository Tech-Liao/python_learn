dic_usr={"John":"123","Marry":"111","Tommy":"123456"}
while True:
    usr_name=input("input user name:")
    if usr_name=="":
        break
    if usr_name in dic_usr:
        usr_passwd=input("input usr_passwd:")
    else:
        print("用户名不正确!")
        continue
    if dic_usr[usr_name]==usr_passwd:
        print("登录成功")
    else:
        print("密码不正确")
        continue
