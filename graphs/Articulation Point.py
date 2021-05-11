def dfs(graph,node,visited,intime,lowtime,parent):
    global timer
    global root
    intime[node]=timer
    lowtime[node]=timer
    timer+=1
    c=0
    visited[node]=True
    for child in graph[node]:
        if not visited[child]:
            if node==root:
                c+=1
            dfs(graph,child,visited,intime,lowtime,node)
            if intime[node]<=lowtime[child] and node!=root:
                print("Articulation Point -->{}".format(node))
            lowtime[node]=min(lowtime[node],lowtime[child])
        else:
            if child!=parent:
                lowtime[node]=min(lowtime[node],intime[child])
    if c>1:
        print("Articulation Point -->{}".format(node))
        



ipt=[[1,2],[2,3],[3,1],[2,4],[2,5],[4,5]]
n=5
graph={}
visited={}
intime={}
lowtime={}
timer=1
root=1
for i in range(1,n+1):
    graph[i]=[]
    visited[i]=False
    intime[i]=None
    lowtime[i]=None
for u,v in ipt:
    graph[u].append(v)
    graph[v].append(u)

dfs(graph,1,visited,intime,lowtime,-1)
