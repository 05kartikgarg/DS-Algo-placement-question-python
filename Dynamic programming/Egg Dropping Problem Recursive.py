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
    4
    2
    
    Output:
    Number of trials when number of eggs is 2 and number of floors is 4: 3

'''
import sys
e,f=map(int,input().split())

def solve(e,f):
    if f==0 or f==1:
        return f
    if e==1:
        return f
    mn=sys.maxsize
    for k in range(1,f+1):
        temp=1+max(solve(e-1,k-1),solve(e,f-k))
        mn=min(mn,temp)
    return mn
print(solve(e,f))
