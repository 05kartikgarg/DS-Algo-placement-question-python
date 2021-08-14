def kahn(graph,visited,indegree):
    queue=[]
    for key in indegree:
        if indegree[key]==0:
            queue.append(key)
            visited[key]=True
    while queue:
        temp=queue.pop(0)
        print(temp)
        for child in graph[temp]:
            if not visited[child]:
                indegree[child]-=1
                if indegree[child]==0:
                    queue.append(child)
                    visited[child]=True
    

ipt=[[1,2],[2,3],[1,6],[3,6],[3,4],[3,5],[1,8],[1,7],[8,9],[7,9]]
n=9
graph={}
visited={}
indegree={}
for i in range(1,n+1):
    graph[i]=[]
    visited[i]=False
    indegree[i]=0

for u,v in ipt:
    graph[u].append(v)
    indegree[v]+=1
    
kahn(graph,visited,indegree)
