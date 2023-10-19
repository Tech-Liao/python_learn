lst_student=["001","李梅",19,"002","刘祥",20,"003","张武",18]
lst_student.append("004")
lst_student.append("刘宁")
lst_student.append(20)
lst_student.append("006")
lst_student.append("梁峰")
lst_student.append(19)
index=lst_student.index("006")
lst_student.insert(index,"005")
lst_student.insert(index+1,"林歌")
lst_student.insert(index+2,20)
print(lst_student)
avg=0
for i in range(1,len(lst_student),3):
   print(lst_student[i])
for i in range(2,len(lst_student),3):
   avg +=lst_student[i]
print(avg/len(lst_student)*3)
