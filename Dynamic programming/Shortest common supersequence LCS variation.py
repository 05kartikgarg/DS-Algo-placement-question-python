m,n=map(int,input().split())
x=input()
y=input()
dp=[[-1 for i in range(1001)] for j in range(1001)]
def SCS(x,y,m,n):
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
    return (m+n)-dp[m][n]
    
print(SCS(x,y,m,n))

'''
m,n=6,6
x=ABCDGH
y=AEDFHR

OUTPUT: 9
'''
