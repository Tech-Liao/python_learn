dic_country={ "China":"Beijing","Ameerica":"Washington","Norway":"Oslo","Japan":"Tokyo","Germany":"Berlin",
        "Canada":"Ottawa","France":"Paris","Thailand":"Bangkok"}
while True:
    capital=input("input capital:")
    if capital == "":
        break
    values= dic_country.values()
    if capital in values:
        for k in dic_country.keys():
            if dic_country[k] == capital:
                print(k)
    else:
        print("未查询到该国家名")
        
