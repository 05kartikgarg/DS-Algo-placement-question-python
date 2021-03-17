import sys
def subsetsum(a,n,s):
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
    return dp[n]



a=list(map(int,input().split()))
n=len(a)
s=sum(a)

temp=subsetsum(a,n,s)
sub1=[]
for i in range((s//2)+1):
    if temp[i]==True:
        sub1.append(i)

mn=sys.maxsize
for i in range(len(sub1)):
    mn=min(mn,s-2*sub1[i])
print(mn)

'''
A= 1 2 7
OUTPUT: 4
'''
