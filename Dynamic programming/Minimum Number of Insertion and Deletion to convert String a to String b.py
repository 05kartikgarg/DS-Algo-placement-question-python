m,n=map(int,input().split())
x=input()
y=input()
dp=[[-1 for i in range(1001)] for j in range(1001)]
def LCS(x,y,m,n):
    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j==0:
                dp[i][j]=0
    for i in range(1,m+1):
        for j in range(1,n+1):
            if x[i-1]==y[j-1]:
                dp[i][j]= 1 + dp[i-1][j-1]
                
            else:
                dp[i][j]= max(dp[i-1][j],dp[i][j-1])
    return dp[m][n]
    
deletion=m-LCS(x,y,m,n)
insertion=n-LCS(x,y,m,n)
print("Total Deletions=",deletion)
print("Total Insertions=",insertion)
'''
m,n=4,3
x=heap
y=pea

OUTPUT: deletions=2, Insertions=1
'''
