dic_repertory={"酱油":50,"醋":60,"盐":100,"糖":120,"鸡精":20,"麻油":40}
dic_change={"酱油":100,"醋":80,"鸡精":50,"耗油":60}
dic_repertory.update(dic_change)
print(dic_repertory)
lst=[[v,k] for k,v in dic_repertory.items()]
lst.sort(reverse=True)
print(lst)
print("Max:{},{}".format(lst[0][1],lst[0][0]))
print("Min:{}.{}".format(lst[-1][1],lst[-1][0]))
