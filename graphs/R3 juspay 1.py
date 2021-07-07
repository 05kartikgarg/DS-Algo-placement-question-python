def checkpath(src,dest,graph,vis):
    vis[src]=1
    for i in graph[src]:
        if not vis[i]:
            checkpath(i,dest,graph,vis)


graph={}
vis={}
n=int(input())
for i in range(n):
    x=int(input())
    graph[x]=[]
    vis[x]=0

e=int(input())
for i in range(e):
    u,v=map(int,input().split())
    graph[u].append(v)

src=int(input())
dest=int(input())
checkpath(src,dest,graph,vis)
print(vis[dest])
