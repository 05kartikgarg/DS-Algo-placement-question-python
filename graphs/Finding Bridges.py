def dfs(graph,node,visited,intime,lowtime,parent):
    global timer
    intime[node]=timer
    lowtime[node]=timer
    timer+=1
    visited[node]=True
    for child in graph[node]:
        if not visited[child]:
            dfs(graph,child,visited,intime,lowtime,node)
            if intime[node]<lowtime[child]:
                print("Bridge",node,"-",child)
            lowtime[node]=min(lowtime[node],lowtime[child])
        else:
            if child!=parent:
                lowtime[node]=min(lowtime[node],intime[child])



ipt=[[1,2],[1,3],[2,4],[3,4],[3,5],[5,6],[5,7],[6,7]]
n=7
graph={}
visited={}
intime={}
lowtime={}
timer=1
for i in range(1,n+1):
    graph[i]=[]
    visited[i]=False
    intime[i]=None
    lowtime[i]=None
for u,v in ipt:
    graph[u].append(v)
    graph[v].append(u)

dfs(graph,1,visited,intime,lowtime,-1)
