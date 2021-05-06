#NlogN + Q*sqrt(N)

phi=[]
def getCount(d,n):
    return phi[n/d]

q=int(input())
while q:
    n=int(input())
    res=0
    i=1
    while i*i<=n:
        if n%i==0:
            d1=i
            d2=n//i
            res+=d1*getCount(d1,n)

            if d1!=d2:
                res+=d2*getCount(d2,n)
        print(res)
    q-=1
                
            
