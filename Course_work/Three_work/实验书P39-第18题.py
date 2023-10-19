s="语文:80,数学:82,英语:90,物理:85,化学:88,美术:80" 
lst_s=s.split(',') 
lst_grate=[]
for ch in lst_s:
   temp=ch.split(":")
   lst_grate.append(int(temp[1]))
print(sum(lst_grate)/len(lst_grate))
