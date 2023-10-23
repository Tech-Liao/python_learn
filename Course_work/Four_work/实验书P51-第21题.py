s="Whether the weather be fine,or whether the weather be not.Whether the weather be cold,or whether the weather be hot.We will weather the whether we like it or not"
s=s.lower()
s=s.replace(","," ")
s=s.replace('.',' ')
s=s.split()
set1=set(s)
print(set1)
