def power(a,n):
    r=1
    while(n):
        if n%2:
            r*=a
            n-=1
        else:
            a*=a
            n/=2
    return r
print(power(2,10))
