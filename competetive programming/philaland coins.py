t=int(input())
while t!=0:
    n=int(input())
    c=0
    while n>0:
        n=n//2
        c+=1
    print(c)

    t-=1
#or
'''
t=int(input())
while t!=0:
    n=int(input())
    print(len("{0:b}".format(n)))
    t-=1
'''
    

