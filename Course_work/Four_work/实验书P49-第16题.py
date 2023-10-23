dic_score={"李刚":93,"陈静":78,"张金柱":88,"赵启山":91,"李鑫":65,"黄宁":83}

lst_score=[(v,k) for k,v in dic_score.items()]
lst_score.sort()
print(lst_score)
