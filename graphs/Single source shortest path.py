edges=[['A','B'],['A','C'],['A','D'],['D','E'],['B','A']]
nodes=['A','B','C','D','E']

def sssp(graph,node,d,distance,parent):
    distance[node]=d
    for child in graph[node]:
        if child != parent:
            sssp(graph,child,distance[node]+1,distance,node)
            
graph={}
distance={}
for key in nodes:
    graph[key]=[]
    distance[key]=None
    
for u,v in edges:
    graph[u].append(v)
    graph[v].append(u)
    
visited=set()
start='A'
distance[start]=0
sssp(graph,start,0,distance,-1)

for key,value in distance.items():
    print(key,value)

