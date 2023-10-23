lst_busstop=["龙江新城市","阳光广场","汉江路","嫩江路","清凉山公园","拉萨路","五台山","莫愁路"]
dic_estate={
        "龙江新城市":["白云园","腾飞园"],"阳光广场":["龙江小区","芳草园"],
        "汉江路":["金信花园","龙凤花园"],"嫩江路":["西城蓝湾","花开四季"]}
estate_dic={}
for k,v in dic_estate.items():
    estate_dic[v[0]]=k
    estate_dic[v[1]]=k
start=input("input start estate:")
end=input("input end estate:")
start_busstop=estate_dic[start]
end_busstop=estate_dic[end]
start_index=lst_busstop.index(start_busstop)
end_index=lst_busstop.index(end_busstop)
print(start_index,end_index)
if start>end:
    print("您需要乘坐反方向线路")
else:
    print("起始站:{},终点站:{},共{}".format(start_busstop,end_busstop,end_index-start_index))
