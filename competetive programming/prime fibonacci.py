def prime(n):
    f=0
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            f=1
            break
    return f

n,m=map(int,input().split())
l1=[]
for i in range(n,m+1):
    if prime(i)==0:
        l1.append(i)
l2=[]
for i in l1:
    for j in l1:
        prod=int(str(i)+str(j))
        if prime(prod)==0 and prod not in l2:
            l2.append(prod)
num2=max(l2)
num1=min(l2)
summ=0
for i in range(len(l2)-2):
    summ=num1+num2
    num1=num2
    num2=summ
print(summ,end='')
    
        
        
