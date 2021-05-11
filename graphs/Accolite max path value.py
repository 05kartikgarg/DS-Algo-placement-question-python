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
        value[ord(nodes[node]) - ord('A')] += 1
        return value
    
    return max(max(dfs(node)) for node in range(len(nodes)))

nodes=["A","B","A","C","A"]
edges=[(0, 1), (0, 2), (2, 3), (3, 4)]
print(longestPath(nodes, edges))

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