dic_student={}

while True:
    name=input("input name:")
    if name=="":
        break
    age=int(input("input {} age:".format(name)))
    Class=input("input {} class:".format(name))
    height=int(input("input {} height:".format(name)))
    weight=int(input("input {} weight:".format(name)))
    dic_student[name]=[Class,age,height,weight]


for k,v in dic_student.items():
    print("{}  {}   {}   {}cm  {}kg".format(v[0],k,v[1],v[2],v[3]))
