lst_odd=[1,3,5,7,9]
lst_even=[2,4,6,8,10]
lst_new=[]
i=0
j=0
while i<5 and j <5:
   if lst_odd[i]>lst_even[j]:
      lst_new.append(lst_even[j])
      j+=1
   else:
      lst_new.append(lst_odd[i])
      i+=1
while j<5:
   lst_new.append(lst_even[j])
   j+=1
while i<5:
   lst_new.append(lst_odd[i])
   i+=1
print(lst_new)
