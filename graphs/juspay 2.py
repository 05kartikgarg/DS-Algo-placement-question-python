from collections import deque
from sys import maxsize as INT_MAX

def BFS(adj, src, dist, paths, n):
	visited = [False] * n
	dist[src] = 0
	paths[src] = 1

	q = deque()
	q.append(src)
	visited[src] = True
	while q:
		curr = q[0]
		q.popleft()
		for x in adj[curr]:
			if not visited[x]:
				q.append(x)
				visited[x] = True
			if dist[x] > dist[curr] + 1:
				dist[x] = dist[curr] + 1
				paths[x] = paths[curr]
			elif dist[x] == dist[curr] + 1:
				paths[x] += paths[curr]

def findShortestPaths(adj, s,dest, n):
	dist = [INT_MAX] * n
	paths = [0] * n
	BFS(adj, s, dist, paths, n)
	print(paths)
	return paths[dest]




n,m,t,c=map(int,input().split())
graph={}
for i in range(1,n+1):
    graph[i]=[]

for i in range(m):
    u,v=map(int,input().split())
    graph[u].append(v)
    #graph[v].append(u)
    
result=[]
for i in range(1,n+1):
    print("r")
    r=findShortestPaths(graph, 1,i, n+1)
    print("r1")
    r1=findShortestPaths(graph, i,n, n+1)
    r=r*r1
    result.append(r)
for i in result:
    print(result[i],end=' ')


