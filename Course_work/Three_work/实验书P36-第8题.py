import random

lst=['A','B','C','D','E']
while True:
   if (lst[2]=='D')+(lst[2]=='B')==1 and (lst[1]=='C')+(lst[3]=='E')==1\
      and (lst[0]=='E')+(lst[4]=='A')==1 and (lst[2]=='C')+(lst[3]=='A')==1\
      and (lst[1]=='B')+(lst[4]=='D')==1:
      print(lst)
      break
   random.shuffle(lst)
