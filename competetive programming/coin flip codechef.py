t=int(input())
for a in range(t):
    g=int(input())
    for j in range(g):
        i,n,q=map(int,input().split())
        count=0
        if n%2==0:
            print(int(n/2))
        else:
            if (i==q):
                print(int(n/2))
            else:
                print(int(n/2) +1)
