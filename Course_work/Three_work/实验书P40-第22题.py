lst_weather=[["周一","16°C","26°C","多云","1级","良"],["周二","17°C","27°C","晴","2级","优"],\
             ["周三","16°C","28°C","晴","3级","优"],["周四","16°C","25°C","阴","2级","良"],\
             ["周五","15°C","24°C","阴","2级","良"],["周六","15°C","25°C","晴","3级","优"],\
             ["周日","14°C","23°C","小雨","3级","良"]]
lst_air=[x[5] for x in lst_weather if x[5]=="优"]
lst_3=[i[0] for i in lst_weather if i[4]<"3级" and i[2]<="25°C"]
lst_4=[(i[0],i[1].split("°C"),i[2].split("°C")) for i in lst_weather ]
lst_4=[(i[0],int(i[1][0]),int(i[2][0])) for i in lst_4]
lst_4=[i[0] for i in lst_4 if i[1]+i[2]<40]
print(lst_air)
print(lst_3)
print(lst_4)
