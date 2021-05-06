def Sieve():
    n=1000000
    prime = [True for i in range(n+1)] 
    p = 2
    while (p  <= n):
        if (prime[p] == True):
            for i in range(p , n+1, p):
                if prime[p]:
                    prime[i] = p
        p += 1
    

