str_in=input("enter a str:")
lst_out=[]
for i in str_in:
   if 'a'<= i <'z' or 'A'<=i<='Z':
      lst_out.append(i)
print(lst_out)
count=[]
for i in lst_out:
    if lst_out.count(i)>1 and i not in count:
       count.append(i)
for i in count:
    lst_out.remove(i)
lst_out=sorted(lst_out)
for ch in lst_out:
   print(ch,end=",")
print()
