s,n=map(int,input().split())
a=list(map(int,input().split()))
r=[]
for i in range(n):
    l,u=map(int,input().split())
    c=0
    for x in a:
        if x<=u and x>=l:
            c+=1
    r.append(c)
for i in r:
    print(i,end=' ')
            
            


    
