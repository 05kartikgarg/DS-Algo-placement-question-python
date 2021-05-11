def isvalid(grid,visited,x,y):
    row=len(grid)
    col=len(grid[0])
    if x<0 or y<0 or x>=row or y>=col or visited[x][y]==1 or grid[x][y]=='N':
        return False
    return True

def bfs(grid,visited,start,end):
    i,j=start[0],start[1]
    queue=[]
    queue.append(start)
    visited[i][j]=1
    distance[i][j]=0
    while queue:
        a,b=queue.pop(0)
        for k,l in [[1,0],[0,1],[-1,0],[0,-1]]:
            if isvalid(grid,visited,a+k,b+l):
                queue.append((a+k,b+l))
                visited[a+k][b+l]=1
                distance[a+k][b+l]=distance[a][b]+1
    print(distance[end[0]][end[1]])


grid=[['S','N','P','P','P'],
      ['P','P','P','N','P'],
      ['P','N','N','N','P'],
      ['P','N','E','P','P']]
row=len(grid)
col=len(grid[0])
visited=[]
distance=[]

for _ in range(row):
    a=[]
    b=[]
    for _ in range(col):
        a.append(0)
        b.append(-1)
    visited.append(a)
    distance.append(b)
for i in range(row):
    for j in range(col):
        if grid[i][j]=='S':
            start=(i,j)
        if grid[i][j]=='E':
            end=(i,j)

bfs(grid,visited,start,end)
