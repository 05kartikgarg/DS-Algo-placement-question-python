def phi(n) : 
    result = n   
    p = 2
    while(p * p<= n) : 
        if (n % p == 0) : 
            while (n % p == 0) : 
                n = n // p 
            result = result * (1.0 - (1.0 / (float) (p))) 
        p = p + 1 
    if (n > 1) : 
        result = result * (1.0 - (1.0 / (float)(n))) 
   
    return (int)(result) 

t=int(input())
while t!=0:
    n=int(input())
    print("ETF("+str(n)+")=",phi(n))
    t-=1
