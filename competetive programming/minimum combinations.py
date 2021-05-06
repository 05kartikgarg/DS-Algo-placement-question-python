def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)

t=int(input())
result=[]
for i in range(t):
    a,b=map(int,input().split())
    result.append(gcd(a,b))

for i in result:
    print(i,end='')
