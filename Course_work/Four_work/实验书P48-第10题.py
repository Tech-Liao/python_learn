dic_city={
        "张三风":["北京","成都"],"李茉绸":["上海","广州","兰州"],"慕容福":["太原","西安","济南","上海"]
        }
names=[]
for k,v in dic_city.items():
    print("{}去过{}个城市".format(k,len(v)))
    if "上海" in v:
        names.append(k)
print("去过上海的有{},他们是{},{}".format(len(names),names[0],names[1]))
