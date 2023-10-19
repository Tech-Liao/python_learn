import random
lst_who=['小马','小羊','小鹿']
lst_where=['草地上','电影院','家里']
lst_what=['看电影','听故事','吃晚饭']
n1=random.randint(0,2)
n2=random.randint(0,2)
n3=random.randint(0,2)
print(lst_who[n1]+"在"+lst_where[n2]+lst_what[n3])
