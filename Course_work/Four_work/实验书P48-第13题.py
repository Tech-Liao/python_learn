str1=input("input a str:")
arr={}
for i in str1:
    if i.isalpha():
        arr[i]=arr.get(i,0)+1
print(arr)
