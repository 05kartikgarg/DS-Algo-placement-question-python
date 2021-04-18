row,col=map(int,input().split())
mat=[]
result=[]
for i in range(row):
    l=list(map(int,input().split()))
    mat.append(l)
for r in range(row):
    for c in range(col):
        if r<(row-3):
            if mat[r][c]==mat[r+1][c]==mat[r+2][c]==mat[r+3][c]:
                result.append(mat[r][c])
        if c<(col-3):
            if mat[r][c]==mat[r][c+1]==mat[r][c+2]==mat[r][c+3]:
                result.append(mat[r][c])
        if (c<(col-3) and r>=3):
            if mat[r][c]==mat[r-1][c+1]==mat[r-2][c+2]==mat[r-3][c+3]:
                result.append(mat[r][c])
        if (c>=3 and r>=3):
            if mat[r][c]==mat[r-1][c-1]==mat[r-2][c-2]==mat[r-3][c-3]:
                result.append(mat[r][c])
# print(result)
if len(result)!=0:
    print("Consective number:",min(result))
else:
    print(-1)
        
'''
6 6
1 3 3 3 3 9
1 6 9 2 3 9
1 2 2 5 4 9
2 2 4 5 7 9
2 4 5 6 7 2
1 2 3 4 5 6

output:2
'''