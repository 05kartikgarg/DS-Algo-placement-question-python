def pairs(n):
    maxi=int(max(str(n)))
    mini=int(min(str(n)))
    dig=(maxi*11)+(mini*7)
    if(dig>99):
        dig=str(dig)[-2]+str(dig)[-1]
    elif(dig<10):
        dig='0'+str(dig)
    return str(dig)

n=int(input())
l=list(map(int,input().split()))
bs=[]
for i in l:
    bs.append(pairs(i))
print(bs)

dic1={}
dic2={}

for in range(n):
    if i%2==0:
        if bs[i][0] not in dic1:
            dic1[bs[i][0]]=1
        else:
            dic1[bs[i][0]]+=1
    else:
        if bs[i][0] not in dic2:
            dic2[bs[i][0]]=1
        else:
            dic2[bs[i][0]]+=1

d={}
for i in dic1:
    if dic1[i]>1:
        d[i]=dic1[i]

for i in dic2:
    if dic2[i]>1:
        if i not in d:
            d[i]=dic2[i]
        else:
            d[i]=max(d[i],dic2[i])

c=0
for i in d:
    if d[i]>2:
        c+=2
    else:
        c+=1

print(c)
        
        
        
