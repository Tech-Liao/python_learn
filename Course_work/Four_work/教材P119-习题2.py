dic={
        "012":[90,94,97,86,85,89,88,85],
        "005":[91,91,92,98,90,96,90,95],
        "108":[96,86,97,96,87,86,86,96],
        "037":[95,95,94,93,97,98,99,95],
        "066":[95,87,94,94,93,99,96,97],
        "020":[89,97,91,95,89,94,97,92]}
dic_sorted=[]
for k,v in dic.items():
    Min=min(v)
    Max=max(v)
    v.remove(Min)
    v.remove(Max)
    avg=sum(v)/len(v)
    dic[k]=avg
    dic_sorted.append((avg,k))
dic_sorted.sort()
dic_sorted=[(k,v) for v,k in dic_sorted]
print(dic_sorted)

