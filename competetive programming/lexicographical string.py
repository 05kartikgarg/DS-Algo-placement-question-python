t= int(input())
while t != 0:
    p=input()
    s=input()
    r=[]
    
    for i in s:
        r.append(p.find(i))
    r.sort()
    for i in r:
        print(p[i],end='')     

    t-=1
