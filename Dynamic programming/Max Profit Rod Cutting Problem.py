# Top- Down approach in dp.


p=list(map(int,input().split()))
c=int(input())
n=len(p)
dp=[[0 for x in range(12)] for x in range(12)] 

for i in range(n+1):
    for j in range(c+1):
        if i==0 or j==0:
            dp[i][j]=0
            
        elif i<=j:
            dp[i][j]=max(p[i-1]+ dp[i][j-i],dp[i-1][j])
            
        else:
            dp[i][j]=dp[i-1][j]
           
print(dp[n][c])


'''
2 1 7 3 5
5
ANS=11
'''
