import sys
graph={}
vis={}
n=int(input())
for i in range(n):
    x=int(input())
    graph[x]=[]
    vis[x]=sys.maxsize

e=int(input())
for i in range(e):
    u,v,t=map(int,input().split())
    graph[u].append([v,t])

src=int(input())
dest=int(input())

s=set()
vis[src]=0
s.add((0,src))
while(len(s)!=0):
    tmp=s.pop()
    u=tmp[1]
    for child in graph[u]:
        v=child[0]
        time=child[1]
        if vis[v]>vis[u]+time:
            if vis[v]!=sys.maxsize:
                s.discard((vis[v],v))
            vis[v]=vis[u]+time
            s.add((vis[v],v))

if vis[dest]==sys.maxsize:
    print("-1")
else:
    print(vis[dest])

'''
4
2
5
7
9
4
2 9 2
7 2 3
7 9 7
9 5 1
7
9
'''

