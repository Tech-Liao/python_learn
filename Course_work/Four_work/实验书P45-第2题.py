dic_student={}

while True:
    name=input("input name:")
    if name=="":
        break
    age=int(input("input score(0-100):"))
    dic_student[name]=age

print(dic_student)
