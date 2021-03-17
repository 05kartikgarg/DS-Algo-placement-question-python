def subsetsum(a,n,s):
    dp=[[False for x in range(s + 1)] for x in range(n + 1)] 

    for i in range(n+1):
        dp[i][0]=True

    for j in range(s+1):
        dp[0][j]=False

        
    for i in range(1,n+1):
        for j in range(1,s+1):            
            if a[i-1]<=j:
                dp[i][j]= dp[i-1][j-a[i-1]] or dp[i-1][j]

            else:
                dp[i][j]=dp[i-1][j]
    return dp[n][s]



a=list(map(int,input().split()))
n=len(a)
s=sum(a)
if s%2!=0:
    print(False)
else:
    print(subsetsum(a,n,s//2))


'''
A= 1 5 5 11
OUTPUT: True
'''
