lst_busstop=["龙江新城市","阳光广场","汉江路","嫰江路","清凉山公园","拉萨路","五台山","莫愁路"]
start=input("enter a start busstop:")
end=input("enter a end busstop:")
start_ind=lst_busstop.index(start)
end_ind=lst_busstop.index(end)
if end_ind<start_ind:
   print("您需要乘坐反方向线路")
else:
   print("从{}站前往{}站需要{}站路".format(start,end,end_ind-start_ind))
