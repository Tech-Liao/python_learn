dic_house={
        "001":["三室一厅",68.69,"南北","简装",37124,35],
        "002":["二室二厅",87.16,"南西","精装",37375,148],
        "003":["三室一厅",61.72,"南北","精装",37266,146],
        "004":["三室二厅",68.18,"南北","精装",68496,79],
        "005":["二室二厅",71.67,"南","简装",33487,105],
        "006":["三室一厅",84.78,"南北","简装",51782,34]
        }
dic_min={}
dic_low={}
for i in range(3):
    Min=1000000000000000
    Max=0
    key=0
    key_1=0
    for k,v in dic_house.items():
        if Min>v[1]*v[4] and k not in dic_min:
            Min=v[1]*v[4]
            key=k
        if Max<v[5] and k not in dic_low:
            Max=v[5]
            key_1=k

    dic_min[key]=Min
    dic_low[key_1]=Max
print(dic_min)
print(dic_low)

