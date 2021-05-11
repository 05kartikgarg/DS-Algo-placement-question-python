def isvalid(grid,visited,x,y):
    row=len(grid)
    col=len(grid[0])
    if x<0 or y<0 or x>=row or y>=col or visited[x][y]==1:
        return False
    return True


def bfs(grid,visited,start):
    queue=[]
    queue.append(start)
    visited[start[0]][start[1]]=1
    while queue:
        a,b=queue.pop(0)
        print(grid[a][b])
        for k,l in [[1,0],[0,1],[-1,0],[0,-1]]:
            if isvalid(grid,visited,a+k,b+l):
                queue.append((a+k,b+l))
                visited[a+k][b+l]=1


grid=[[3,1,5],[7,8,2],[14,11,9]]
row=len(grid)
col=len(grid[0])
visited=[]
for _ in range(row):
    temp=[]
    for _ in range(col):
        temp.append(0)
    visited.append(temp)

bfs(grid,visited,(0,0))
