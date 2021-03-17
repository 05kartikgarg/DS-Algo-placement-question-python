w=list(map(int,input().split()))
p=list(map(int,input().split()))
c=int(input())
n=len(w)

def knapsack(w,p,c,n):
    if c==0 or n==0:
        return 0

    if w[n-1]<=c:
        return max(p[n-1]+knapsack(w,p,c-w[n-1],n-1),knapsack(w,p,c,n-1))

    elif w[n-1]>c:
        return knapsack(w,p,c,n-1)
    
max_profit = knapsack(w,p,c,n)  
print(max_profit )
