grade = [90,95,98]
sum = sum(grade)
average = sum/3
max_course = max(grade)
min_course = min(grade)

all_sum = 0.5*grade[0]+0.3*grade[1]+0.2*grade[2]
print("三门成绩和:{:.2f}".format(sum))
print("三门成绩的平均：{:.2f}".format(average))
print("三门成绩的最小值：",min_course)
print("三门成绩的最大值：",max_course)
print("总评成绩：",all_sum)
