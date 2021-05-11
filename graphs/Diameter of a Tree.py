def dfs(graph,node,visited):
    visited[node]=True
    sm=0
    for child in graph[node]:
        if not visited[child]:
            sm=max(sm,dfs(graph,child,visited))
    return sm+1

def dfs1(graph,node,visited):
    visited[node]=True
    sm=0
    temp=node
    for child in graph[node]:
        if not visited[child]:
            (tval,tnode)=dfs1(graph,child,visited)
            if tval>sm:
                temp=tnode
                sm=tval
    return [sm+1,temp]



ipt=[[1,2],[2,4],[2,5],[2,6],[1,3],[3,7],[1,8],[6,10],[1,9]]
graph={}
visited={}
n=10
for i in range(1,n+1):
    graph[i]=[]
    visited[i]=False
for u,v in ipt:
    graph[u].append(v)
    graph[v].append(u)
    
temp=dfs1(graph,1,visited)
v={}
for i in range(1,n+1):
    v[i]=False
print(dfs(graph,temp[1],v))
