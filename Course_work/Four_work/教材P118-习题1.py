

dicTXL={"小新":("13913000001","18191220001"),"小亮":("13913000002","18191220002"),"小刚":("13913000003","18191220003")}
dicOther={"大刘":("13914000001","18191230001"),"大王":("13914000002","18191230002"),"大张":("13914000003","18191230003")}

dicTXL.update(dicOther)
dicWX={"小新":"xx9907","小刚":"gang1004","大王":"jack_w","大刘":"liu666"}
for k,v in dicTXL.items():
    dicTXL[k]=[dicWX.get(k,v[0]),v[0],v[1]]
temp=dicTXL.get('大王')
temp[1]='13914000004'
dicTXL['大王']=temp
while True:
    names=input("input name:")
    if names=="":
        break
    if names in dicTXL:
        temp=dicTXL[names]
        print("微信号:{},手机号,{},qq号:{}".format(temp[0],temp[1],temp[2]))
    else:
        print("无该同学的联系方式")

