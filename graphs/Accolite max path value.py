import functools, collections

def longestPath(nodes, edges):
    graph = collections.defaultdict(list)
    for i, j in edges:
        graph[i].append(j)
    
    def cyclic(node, visited):
        if node not in visited:
            visited.add(node)
            return any(cyclic(nei, visited) for nei in graph[node])
        return True
    if any(cyclic(node, set()) for node in range(len(nodes))):
        return None
    
    @functools.lru_cache(None)
    def dfs(node):
        value = [0] * 26
        for nei in graph[node]:
            value = [max(a, b) for a, b in zip(value, dfs(nei))]
        value[ord(nodes[node]) - ord('a')] += 1
       
        return value
    
    return max(max(dfs(node)) for node in range(len(nodes)))

def beauty(n,m,s,x,y):
    nodes=[i for i in s]
    edges=[]
    for j in range(m):
        edges.append((x[j]-1,y[j]-1))
    
    ans=longestPath(nodes, edges)
    if  ans==None:
        ans=-1
    return ans

n=int(input())
m=int(input())
s=input()
x=list(map(int,input().split()))
y=list(map(int,input().split()))
print(beauty(n,m,s,x,y))

'''

tests = [
         ("A", [(0, 0)], None), 
         ("ABACA", [(0, 1), (0, 2), (2, 3), (3, 4)], 3),
         ("BAA", [(0, 1), (0, 2)], 1),
         ("BAA", [(0, 1), (2, 0)], 2)
        ]

for nodes, edges, ans in tests:
    assert longestPath(nodes, edges) == ans
    '''
