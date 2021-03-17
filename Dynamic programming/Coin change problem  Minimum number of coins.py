import sys
def coinchangemin(a,n,s):
    dp=[[0 for x in range(s + 1)] for x in range(n + 1)] 

    for i in range(n+1):
        dp[i][0]=0

    for j in range(1,s+1):
        dp[0][j]=sys.maxsize-1

    for j in range(1,s+1):
        if j%a[0]==0:
            dp[1][j]=j//a[0]
        else:
            dp[1][j]=sys.maxsize-1

        
    for i in range(2,n+1):
        for j in range(1,s+1):            
            if a[i-1]<=j:
                dp[i][j]= min(dp[i][j-a[i-1]]+1 , dp[i-1][j])

            else:
                dp[i][j]=dp[i-1][j]
    return dp[n][s]



coin=list(map(int,input().split()))
s=int(input())
n=len(coin)
print(coinchangemin(coin,n,s))



'''
A= 1 2 3
S= 4
OUTPUT: 2
'''
