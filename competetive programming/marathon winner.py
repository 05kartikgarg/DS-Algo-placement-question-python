from collections import Counter

n=int(input())
t=int(input())

participant=[]
l1=[]
l2=[]

for i in range(n):
    k=list(map(int,input().split()))
    d=k[-1]
    k.pop()

    b=[]
    sum1=0
for i in k:
    r=i*d
    sum1+=r
    b.append(sum1)
l1.append(b)

for i in range(t):
    l2.append(list(list(zip(*l1))[i]))

for i in range(1,len(l2),2):
    m=max(l2[i])
    for j in range(len(l2[i])):
        if m==l2[i][j]:
            participant.append(j+1)

res=dict(Counter(participant))

values=list(res.values())
keys=list(res.keys())

print(keys[values.index(max(values))])
    
