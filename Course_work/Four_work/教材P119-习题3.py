course1={"李雷","张玉","王晓刚","陈红静","方向","司马清"}
course2={"施然","李芳芳","刘潇","方向","孙一航","黄煌"}
course3={"陈红静","方向","刘培良","张玉","施小然","司马清"}
set1=course1 | course2 | course3
print("有{}位没选课".format(25-len(set1)))
count1=0
for i in course1:
    if i in course2 and i not in course3:
        count1+=1
    elif i not in course2 and i in course3:
        count1+=1
print("有{}位同学选修两门课".format(count1))
set2=course1 & course2 & course3
print("有{}位同学".format(len(set2)))
set3=(course1 - (course2 | course3)) | (course2-(course1 | course3)) | (course3 - (course1 | course2))  
print("有{}位同学".format(len(set3)))

