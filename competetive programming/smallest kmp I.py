# cook your dish here
t=int(input())
while t!=0:
    s=list(input().lower())
    p=input().lower()
    for i in p:
        s.remove(i)
    s.append(p)
    s.sort()
    for i in s:
        print(i,end='')
    print()
    t-=1
