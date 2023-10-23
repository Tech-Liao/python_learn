s="When in the course of human events, it becomes necessary for one people todissolve the political bands which have connected them with another, and to assume among the powers of the earth, the separate and equal station to which the laws Nature and Nature’s God entitle them, a decent respect to the opinions of mankind requires that they should declare the causes which impelthem to the separation."
s=s.split(" ")
dic_word={}
for x in s:
    dic_word[x]=dic_word.get(x,0)+1

print(dic_word)
dic_max={}
for i in range(5):
    Max=0
    key=0
    for k,v in dic_word.items():
        if v>Max and k not in dic_max:
            Max=v
            key=k
    dic_max[key]=Max
print(dic_max)
    
