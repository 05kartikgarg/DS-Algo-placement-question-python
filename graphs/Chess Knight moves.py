def isvalid(grid,visited,x,y):
    row=len(grid)
    col=len(grid[0])
    if x<0 or y<0 or x>=row or y>=col or visited[x][y]==1:
        return False
    return True

child=[[2,1],[-2,1],[-1,2],[1,2],[2,-1],[-2,-1],[-1,-2]]

def bfs(grid,visited,distance,start,end):
    global child
    i,j=start[0],start[1]
    queue=[]
    queue.append((i,j))
    visited[i][j]=1
    distance[i][j]=0
    while queue:
        x,y=queue.pop(0)
        for u,v in child:
            if isvalid(grid,visited,x+u,y+v):
                queue.append((x+u,y+v))
                visited[x+u][y+v]=1
                distance[x+u][y+v]=distance[x][y]+1
    for item in distance:
        print(item)
    print(distance[end[0]][end[1]])

grid=[['','B','',''],['','','',''],['','A','',''],['','','',''],['','','','']]
visited=[]
distance=[]
row=len(grid)
col=len(grid[0])
for i in range(row):
    t1=[]
    t2=[]
    for j in range(col):
        t1.append(0)
        t2.append(-1)
    visited.append(t1)
    distance.append(t2)

for i in range(row):
    for j in range(col):
        if grid[i][j]=='A':
            start=(i,j)
        if grid[i][j]=='B':
            end=(i,j)
            
bfs(grid,visited,distance,start,end)
