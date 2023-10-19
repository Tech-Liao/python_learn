import random
lst_suit=["黑桃","红桃","梅花","方块"]
lst_face=['3','4','5','6','7','8','9','10','J','Q','k','A','2']
lst=[lst_face[i]+' '+lst_suit[j] for i in range(len(lst_face)) for j in range(len(lst_suit))]
random.shuffle(lst)
while True:
    num=int(input("Enter a num(0-51):"))
    n=random.randint(0,51)
    if lst[num]>lst[n]:
       print("恭喜，您赢了")
    elif lst[num]<lst[n]:
       print("很遗憾，您输了")
    else:
       print("咱们平手了")
    print(num,n,lst[num],lst[n])


