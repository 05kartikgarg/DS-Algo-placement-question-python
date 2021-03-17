m,n=map(int,input().split())
x=input()
y=input()
dp=[[-1 for i in range(1001)] for j in range(1001)]
def LCS(x,y,m,n):
    if m==0 or n==0:
        return 0
    if dp[m][n]!=-1:
        return dp[m][n]
    
    if x[m-1]==y[n-1]:
        dp[m][n]= 1 + LCS(x,y,m-1,n-1)
        return dp[m][n] 
    else:
        dp[m][n]= max(LCS(x,y,m-1,n),LCS(x,y,m,n-1))
        return dp[m][n]
    
print(LCS(x,y,m,n))

'''
m,n=6,6
x=ABCDGH
y=AEDFHR

OUTPUT: 3
'''
