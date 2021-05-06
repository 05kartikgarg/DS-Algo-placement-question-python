def primefact(n):
    for i in range(2,int(n**0.5)+1):
        if(n%i==0):
            c=0
            while(n%i==0):
                c+=1
                n/=i
            print(i,"^",c)
    if n>1:
            print(n,"^",1)
primefact(20)
            
