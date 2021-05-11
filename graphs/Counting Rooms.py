def isvalid(grid,visited,x,y):
    row=len(grid)
    col=len(grid[0])
    if x<0 or y<0 or x>=row or y>=col or visited[x][y]==1 or grid[x][y]==1:
        return False
    return True

def dfs(grid,visited,start):
    i,j=start[0],start[1]
    visited[i][j]=1
    sm=0
    for a,b in [[1,0],[0,1],[-1,0],[0,-1]]:
        if isvalid(grid,visited,i+a,j+b):
            sm+=dfs(grid,visited,(i+a,j+b))

    return sm+1



grid=[[0,1,0,0,0,0],[0,1,0,0,0,0],[1,0,1,0,1,1],[0,0,1,1,0,0],[1,0,0,1,0,0],[1,1,0,1,0,0]]
row=len(grid)
col=len(grid[0])
visited=[]
for _ in range(row):
    temp=[]
    for _ in range(col):
        temp.append(0)
    visited.append(temp)
ans=[]
for i in range(row):
    for j in range(col):
        if visited[i][j]==0 and grid[i][j]==0:
            temp=dfs(grid,visited,(i,j))
            ans.append(temp)
print(ans)
