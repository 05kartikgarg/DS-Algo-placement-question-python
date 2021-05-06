import math
t=int(input())
while t!=0:
    n=int(input())
    def prime(n):
        if n==1:
            return False
        for i in range(2,int(math.sqrt(n))):
            if(n%i==0):
                return False

        return True
    
    if prime(n):
        print("yes")
    else:
        print("no")
    t-=1
