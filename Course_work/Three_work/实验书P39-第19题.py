lst=[("triangle","shape"),("red","color"),("square","shape"),("yellow","color"),("green","color"),("circle","shape")]
lst_a=[(v,k) for k,v in lst]
lst_a=sorted(lst_a)
print(lst_a)
lst_color=[k[1] for k in lst_a if k[0]=='color']
print(lst_color)
