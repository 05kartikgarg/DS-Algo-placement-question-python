# Top- Down approach in dp.

w=list(map(int,input().split()))
p=list(map(int,input().split()))
c=int(input())
n=len(w)
dp=[[0 for x in range(c + 1)] for x in range(n + 1)] 

for i in range(n+1):
    for j in range(c+1):
        if i==0 or j==0:
            dp[i][j]=0
            
        elif w[i-1]<=j:
            dp[i][j]=max(p[i-1]+ dp[i-1][j-w[i-1]],dp[i-1][j])
            
        else:
            dp[i][j]=dp[i-1][j]
            
print(dp[n][c])


'''
1 2 5 6 7
1 6 18 22 28
11
ANS=40
'''
