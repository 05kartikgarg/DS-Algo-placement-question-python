m,n=map(int,input().split())
x=input()
y=input()
dp=[[-1 for i in range(1001)] for j in range(1001)]
def LCS(x,y,m,n):
    result=0
    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j==0:
                dp[i][j]=0
                
    for i in range(1,m+1):
        for j in range(1,n+1):
            if x[i-1]==y[j-1]:
                dp[i][j]= 1 + dp[i-1][j-1]
                result =max(result, dp[i][j])
                
            else:
                dp[i][j]= 0
    return result
    
print(LCS(x,y,m,n))

'''
m,n=7,7
X = abcdxyz
y = xyzabcd 

OUTPUT: 4
'''
