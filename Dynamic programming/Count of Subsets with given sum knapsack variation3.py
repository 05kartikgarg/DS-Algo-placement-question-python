def countofsubsetsum(a,n,s):
    dp=[[0 for x in range(s + 1)] for x in range(n + 1)] 

    for i in range(n+1):
        dp[i][0]=1

    for j in range(1,s+1):
        dp[0][j]=0

        
    for i in range(1,n+1):
        for j in range(1,s+1):            
            if a[i-1]<=j:
                dp[i][j]= dp[i-1][j-a[i-1]] + dp[i-1][j]

            else:
                dp[i][j]=dp[i-1][j]
    return dp[n][s]



a=list(map(int,input().split()))
s=int(input())
n=len(a)
print(countofsubsetsum(a,n,s))



'''
A= 2 3 8 5 10
S= 10
OUTPUT: 3
'''
