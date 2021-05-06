'''
a^(m-1)congruent to 1 * mod m

a^(m-2)congruent to a^-1 * mod m

m must be prime and a&m must be co-prime

'''
def power(a,n,m):
    res=1
    while(n):
        if n%2==1:
            res=(res*a)%m
            n-=1
        else:
            n/=2
            a=(a*a)%m
    return res

t=int(input())
while t!=0:
    a,m=map(int,input().split())
    print("a^-1= ",power(a,m-2,m))
    t-=1
