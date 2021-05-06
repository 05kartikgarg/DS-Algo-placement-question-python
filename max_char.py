n,m=map(int,input().split())
mat=[]
l=[]
result=[]
for i in range(n):
    temp=list(map(str,input().split()))
    mat.append(temp)
    l.extend(temp)
s=list(set(l))
d={}
for i in s:
    d[i]=l.count(i)
m=max(d.values())
for i in d:
    if d[i]==m:
        result.append(i)
print(' '.join(result))
