ch = input("请输入一个字符：")
if 'a'<=ch<='z' or 'A'<=ch<='Z':
   print("输入的是英文字符")
elif '0'<=ch<='9':
   print("输入的是数字字符")
else:
   print("输入的是其他字符")
