a=list(map(int,input().split()))
s=int(input())
n=len(a)
dp=[[False for x in range(s + 1)] for x in range(n + 1)] 

for i in range(n+1):
    dp[i][0]=True

for j in range(1,s+1):
    dp[0][j]=False

    
for i in range(1,n+1):
    for j in range(1,s+1):            
        if a[i-1]<=j:
            dp[i][j]= dp[i-1][j-a[i-1]] or dp[i-1][j]

        else:
            dp[i][j]=dp[i-1][j]
print(dp[n][s])

'''
A= 3 34 4 12 5 2
S= 9
OUTPUT: True
'''
