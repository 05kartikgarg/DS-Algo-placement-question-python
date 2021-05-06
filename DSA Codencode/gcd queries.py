def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)
t=int(input())
while t!=0:
    n,q=map(int,input().split())
    a=list(map(int,input().split()))
    pre=[0]*(n+1)
    suff=[0]*(n+1)
    for i in range(1,n+1):
        pre[i]=gcd(pre[i-1],a[i-1])
    for j in range(n,0,-1):
        suff[i-1]=gcd(suff[i],a[i-1])
    for k in range(q):
        l,r=map(int,input().split())
        print(gcd(pre[l-1],suff[r]))
        
    t-=1
