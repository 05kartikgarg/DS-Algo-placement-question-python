t=int(input())
while t!=0:
    x,y,k,n=map(int,input().split())
    result=0
    for _ in range(n):
        p,c=map(int,input().split())
        r=x-y
        if r<=p and c<=k:
            result=1
            break
    if(result==1):
        print("LuckyChef")
    else:
        print("UnluckyChef")
        
    t-=1
