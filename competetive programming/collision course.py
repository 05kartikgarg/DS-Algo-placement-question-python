t=int(input())
d={}
collision=0

for i in range(t):
    x,y,speed=list(map(int,input().split()))

    sq_time=(x**2+y**2)/(speed**2)
    if(d.get(sq_time)==None):
        d[sq_time]=1
    else:
        d[sq_time]=d[sq_time]+1

for keys in d:
    if(d[keys]!=1):
        collision+=(d[keys]*(d[keys]-1))/2

print(int(collision))
