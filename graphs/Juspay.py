def bfs(graph,src,des,n,pred,dist):
    queue=[]
    visited=[False for i in range(1,n+1)]
    for i in range(0,n):
        dist[i]=1000000
        pred[i]=-1
    visited[src] = True
    dist[src] = 0
    queue.append(src)

    while (len(queue) != 0):
        u = queue[0]
        queue.pop(0)
        for i in range(len(graph[u])):
         
            if (visited[graph[u][i]] == False):
                visited[graph[u][i]] = True
                dist[graph[u][i]] = dist[u] + 1
                pred[graph[u][i]] = u
                queue.append(graph[u][i])
  
                if (graph[u][i] == des):
                    return True
    return False

     

def printShortestDistance(graph, s, dest, n):
    pred=[0 for i in range(0,n)]
    dist=[0 for i in range(0,n)]

    if (bfs(graph, s, dest, n, pred, dist) == False):
        print(-1)

    path = []
    crawl = dest

    path.append(crawl)
     
    while (pred[crawl] != -1):
        path.append(pred[crawl])
        crawl = pred[crawl]

    if t<c:
        if c%t!=0:
            print(dist[dest]*c+(t-c%t))
        else:
            print((dist[dest])*c)
    else:
        if((t//c+1)>=dist[dest] or t%c==0):
            print((dist[dest])*c)
        else:
            print(t-(c-(t%c)))*(t//c)+(dist[dest])*c
        

n,m,t,c=map(int,input().split())
graph={}
for i in range(1,n+1):
    graph[i]=[]

for i in range(m):
    u,v=map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

printShortestDistance(graph, 1, n, n+1)


'''
5 5 3 5
1 2
1 3
2 4
1 4
2 5
'''
