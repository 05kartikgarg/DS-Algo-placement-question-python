edges=[['A','B'],['A','C'],['A','D'],['D','E'],['B','A'],['F','H'],['F','G'],['I','J']]
nodes=['A','B','C','D','E','F','G','H','I','J','K']

def dfs(graph,node,visited):
    visited.add(node)
    sm=0
    for child in graph[node]:
        if child not in visited:
            sm+=dfs(graph,child,visited)
    return sm+1

graph={}
for key in nodes:
    graph[key]=[]
    
for u,v in edges:
    graph[u].append(v)
    graph[v].append(u)
    
visited=set()
answer=[]
for item in nodes:
    if item not in visited:
        temp=dfs(graph,item,visited)
        answer.append(temp)

print(answer)
