myDict={ "方糖":99,"X1":499,"魔盒":399,"曲奇":299}
Max=0
Sum=0
for k,v in myDict.items():
    if v>Max:
        Max=v
    Sum+=v
    print(k,v,sep="········")
print(Sum/len(myDict),Max)
