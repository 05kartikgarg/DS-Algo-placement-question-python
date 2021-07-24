def find(graph,node):
    if graph[node]<0:
        return node
    else:
        temp=find(graph,graph[node])
        graph[node]=temp
        return temp

def union(graph,a,b,answer):
    ta=a
    tb=b
    a=find(graph,a)
    b=find(graph,b)
    if a==b:
        pass
    else:
        answer.append([ta,tb])
        if graph[a]<graph[b]:
            graph[a]+=graph[b]
            graph[b]=a
        else:
            graph[b]+=graph[a]
            graph[a]=b


ipt=[[1,2,1],[1,3,3],[2,6,4],[3,6,2],[3,4,1],[4,5,5],[7,5,7]]
n=7
answer=[]
ipt=sorted(ipt,key=lambda ipt:ipt[2])
graph=[-1]*(n+1)
for u,v,d in ipt:
    union(graph,u,v,answer)
for item in answer:
    print(item)