def power(a,n,d):
    res=1
    while(n):
        if n%2==1:
            res=((res%d)*(a%d))%d
            n-=1
        else:
            a=((a%d)*(a%d))%d
            n/=2
    return res


def gcd(a,b,n):
    mod=1000000007
    if a==b:
        return (power(a,n,mod)+power(b,n,mod))%mod

    candidate=1
    num=a-b

    for i in range(1,int(num**0.5)+1):
        if num%i==0:
            tmp=(power(a,n,i)+power(b,n,i))%i
        if tmp==0:
            candidate=max(candidate,i)
        tmp=((power(a,n,num//i)+power(b,n,num//i))%num//i)
        if tmp==0:
            candidate=max(candidate,num//i)
    return candidate%mod

t=int(input())
while t!=0:
    a,b,n=map(int,input().split())
    print(gcd(a,b,n))
    t-=1
 
