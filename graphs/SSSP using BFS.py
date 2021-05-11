def bfs(graph,visited,distance):
    queue=[]
    queue.append(1)
    visited[1]=True
    distance[1]=0
    while queue:
        temp=queue.pop(0)
        #print(temp)
        for child in graph[temp]:
            if not visited[child]:
                queue.append(child)
                visited[child]=True
                distance[child]=distance[temp]+1


ipt=[[1,2],[2,3],[1,6],[3,6],[3,4],[3,5],[1,8],[1,7],[8,9],[7,9]]
n=9
graph={}
visited={}
distance={}
for i in range(1,n+1):
    graph[i]=[]
    visited[i]=False
    distance[i]=None

for u,v in ipt:
    graph[u].append(v)
    graph[v].append(u)

bfs(graph,visited,distance)

for key,val in distance.items():
    print(key,val)



