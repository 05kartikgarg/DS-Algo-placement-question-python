'''
#method 1: Recursive

def D(n):
    if n==0:
        return 1
    if n==1:
        return 0
    if n==2:
        return 1

    return (n-1)*(D(n-1)+D(n-2))

n=int(input())
print(D(n)%1000000007)
'''
#method 2: Dynamic

def countder(n):
    D=[0 for i in range(n+1)]

    D[0]=1
    D[1]=0
    D[2]=1

    for i in range(3,n+1):
        D[i]=(i-1)*(D[i-1]+D[i-2])

    return D[n]

n=int(input())
print(countder(n)%1000000007)




        
