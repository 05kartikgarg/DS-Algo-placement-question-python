def dfs(graph,node,visited,distance):
    visited[node]=True
    sm=0
    for child in graph[node]:
        if not visited[child]:
            sm=sm+dfs(graph,child,visited,distance)
    distance[node]=sm+1
    return distance[node]


ipt=[[1,2],[2,4],[2,5],[2,6],[1,3],[3,7],[1,8],[6,10],[1,9]]
graph={}
visited={}
distance={}
n=10
for i in range(1,n+1):
    graph[i]=[]
    visited[i]=False
    distance[i]=None
for u,v in ipt:
    graph[u].append(v)
    graph[v].append(u)

dfs(graph,1,visited,distance)
print(distance)
