'''
Egg Dropping using Recursion
Problem statement: You are given N floor and K eggs. You have to minimize the number of times
you have to drop the eggs to find the critical floor where critical floor means the floor
beyond which eggs start to break. Assumptions of the problem:

If egg breaks at ith floor then it also breaks at all greater floors.
If egg does not break at ith floor then it does not break at all lower floors.
Unbroken egg can be used again.
Note: You have to find minimum trials required to find the critical floor not the critical
floor.

Example:
Input:
    2 4
    Output:
    Number of trials when number of eggs is 2 and number of floors is 4: 3

'''
import sys
e,f=map(int,input().split())
dp=[[-1 for i in range(1001)]for i in range(1001)]
def solve(e,f):
    if f==0 or f==1:
        return f
    if e==1:
        return f
    if dp[e][f]!=-1:
        return dp[e][f]
        
    mn=sys.maxsize
    for k in range(1,f+1):
        if dp[e-1][k-1]!=-1:
            low=dp[e-1][k-1]
        else:
            low=solve(e-1,k-1)
            dp[e-1][k-1]=low
            
        if dp[e][f-k]!=-1:
            high=dp[e][f-k]
        else:
            high=solve(e,f-k)
            dp[e][f-k]=high
            dp[e-1][k-1]=low
            
        temp=1+max(low,high)
        mn=min(mn,temp)
    dp[e][f]=mn
    return dp[e][f]
print(solve(e,f))
