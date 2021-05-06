t=int(input())
r=[]
while t!=0:
    n=int(input())
    l=list(map(int,input().split()))
    arr=[]   
    while len(l)>=2:
        
        l.sort()
        s=l[0]+l[1]
        arr.append(s)
        l.pop(0)
        l.pop(0)
        l.append(arr[-1])
    r.append(sum(arr))

    for i in r:
        print(i)
    t-=1


    
