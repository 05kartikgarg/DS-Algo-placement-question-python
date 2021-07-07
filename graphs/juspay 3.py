def secondmin(graph,src,dest,l,c,t,ans,res,green,ch):
    if ans//t>ch:
        ch+=1
    if src==dest:
        res.append(ans)
        return
    for i in graph[src]:
        if str(i) not in l[:-1].split():
            if green:
                secondmin(graph,i,dest,l+str(i)+" ",c,t,ans+c,res,green,ch)
            else:
                a=ans%t
                secondmin(graph,i,dest,l+str(i)+" ",c,t,ans+c+t-a,res,not green,ch)
    return


n,m,t,c=map(int,input().split())
graph={}
for i in range(1,n+1):
    graph[i]=[]

for i in range(m):
    u,v=map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

l="1 "
res=[]
green=True
ch=0
r=secondmin(graph,1,n,l,c,t,0,res,green,ch)
res=list(set(res))
res.sort()
if len(res)>1:
    print(res[1])
else:
    print(-1)
