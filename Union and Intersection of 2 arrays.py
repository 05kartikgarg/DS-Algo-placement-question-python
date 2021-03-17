n=int(input())
m=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

#union
for i in b:
    a.append(i)
uni=list(set(a))
print('union=',uni)

#intersection
intersect=[]
if m<=n:
    for i in b:
        if i in a:
            intersect.append(i)
else:
    for i in a:
        if i in b:
            intersect.append(i)
print("Intersection=",intersect)
