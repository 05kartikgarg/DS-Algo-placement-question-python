from math import sqrt
n,k=[int(x) for x in input().split()]
print(n,k)
c=0
fact=[]

for i in range(1,int(sqrt(n)+1)):
    if n%i==0:
        fact.append(i)
        fact.append(n//i)
        c+=2
fact.sort()
fact=list(set(fact))
#print(fact)
if c>k:
    print(fact[-k])
else:
    print(1)
