
dic={}
ch=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
while True:
    offset=int(input("input a num:"))
    if offset<0:
        break
    for i in ch:
        if ord('a')<=ord(i)+offset<=ord('z'):
            dic[i]=chr(ord(i)+offset)
        else:
            temp=(ord(i)+offset)%ord('z')+ord('a')-1
            dic[i]=chr(temp)
    print(dic)
    print(len(dic))
    break
