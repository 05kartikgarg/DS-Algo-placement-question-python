t=int(input())
while t!=0:
    n=int(input())
    s=input()
    d={}
    for i in s:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1

    print(d)

    result=all(value%2 == 0 for value in d.values())

    if result==True:
        print("YES")
    else:
        print("NO")


    t-=1
