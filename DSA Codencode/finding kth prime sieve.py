def SieveOfEratosthenes(n):
    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * p, n+1, p):
                prime[i] = False
            p += 1
    l=[]
    for p in range(2, n+1):
        if prime[p]:
            l.append(prime[p])
			
SieveOfEratosthenes(50000000)
t=int(input())
while t!=0:
    n=int(input())
    print(l[n-1])
    t-=1
    


