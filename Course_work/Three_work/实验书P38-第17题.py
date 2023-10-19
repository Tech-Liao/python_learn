import math
lst_area=[]
lst_sides=[3,4,5,6,6,6,4,4,3]
for i in range(0,len(lst_sides),3):
   avg=(lst_sides[i]+lst_sides[i+1]+lst_sides[i+2])//2
   lst_area.append(math.sqrt(avg*(avg-lst_sides[i])*(avg-lst_sides[i+1])*(avg-lst_sides[i+2])))
print(lst_area)
