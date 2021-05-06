a,b=map(int,input().split()))
l=list(map(int,input().split())))

for i in range(b):
    max1=max(l)
    l.remove(max1)
    l.append(max1//2)
print(sum(l),end='')
