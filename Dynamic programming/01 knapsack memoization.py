w=list(map(int,input().split()))
p=list(map(int,input().split()))
c=int(input())
n=len(w)
dp=[[-1 for i in range(1001)] for j in range(1001)]


def knapsack(w,p,c,n):
    if n==0 or c==0:
        return 0
    
    if dp[n][c]!=-1:
        return dp[n][c]

    if w[n-1]<=c:
        dp[n][c]=max(p[n-1]+knapsack(w,p,c-w[n-1],n-1),knapsack(w,p,c,n-1))
        return dp[n][c]

    elif w[n-1]>c:
        dp[n][c]=knapsack(w,p,c,n-1)
        return dp[n][c]
    
max_profit = knapsack(w,p,c,n)  
print(max_profit )

'''
1 2 5 6 7
1 6 18 22 28
11
ANS=40
'''
