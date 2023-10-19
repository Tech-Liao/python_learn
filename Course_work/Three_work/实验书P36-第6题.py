lst_student=[ ["001","李梅",19],
              ["002","刘祥",20],
              ["003","张武",18]]

lst_student.append(["004","刘宁",20])
lst_student.append(["006","梁峰",19])
lst_student.insert(4,["005","林歌",20])
print(lst_student[2])
for lst in lst_student:
   print(lst[1])
   if lst[2]>19:
      print(lst)

