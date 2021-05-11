def find(graph,node):
    if graph[node]<0:
        return node
    else:
        temp=find(graph,graph[node])
        graph[node]=temp
        return temp

def union(graph,a,b):
    ta=a
    tb=b
    a=find(graph,a)
    b=find(graph,b)
    if a==b:
        print("cannot be connected",ta,tb)
    else:
        if graph[a]==graph[b]:
            graph[b]+=graph[a]
            graph[a]=b
        else:
            if graph[a]<graph[b]:
                graph[a]+=graph[b]
                graph[b]=a
            else:
                graph[b]+=graph[a]
                graph[a]=b

n=7
graph={}
for i in range(7):
    graph[i]=-1

ipt=[[0,1],[1,2],[2,3],[4,5],[1,3]]
for u,v in ipt:
    union(graph,u,v)
print(graph)
