def timeconvert(s):
    if s[-2:]=='AM' and s[:2]=='12':
        return int('00'+s[3:5])
    elif s[-2:]=='AM':
        return int(s[:2]+s[3:5])
    elif s[-2:]=='PM' and s[:2]=='12':
        return int('12'+s[3:5])
    else:
        return 1200+int(s[:2]+s[3:5])

# print(timeconvert('12:45 PM'))

t=int(input())
while t!=0:
    k=''
    p=input()
    pf=timeconvert(p)
    n=int(input())
    for i in range(n):
        s=input()
        l,r=s[:8],s[9:]
        lf=timeconvert(l)
        rf=timeconvert(r)
        if lf<=pf<=rf:
            k+='1'
        else:
            k+='0'
    print(k)
    
    t-=1