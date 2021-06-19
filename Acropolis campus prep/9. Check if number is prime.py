n=int(input())

def isprime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
            break
    return True
print(isprime(n))
