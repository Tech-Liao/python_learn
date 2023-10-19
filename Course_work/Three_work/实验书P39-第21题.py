lst_score=[9,10,8,9,10,7,6,8,7,8]
Max=max(lst_score)
lst_score.remove(Max)
Min=min(lst_score)
lst_score.remove(Min)
print(lst_score)
avg=sum(lst_score)/len(lst_score)
print(avg)
