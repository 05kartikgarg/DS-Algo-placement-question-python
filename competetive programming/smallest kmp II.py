from copy import deepcopy
t=int(input())
while t!=0:
    s=list(input().lower())
    p=input().lower()
    for i in p:
        s.remove(i)
    s.sort()
    ne=deepcopy(s)
    ne.append(p[0])
    ne=sorted(ne,reverse=True)
    if p[0] not in s:
        print(''.join(s[0:len(ne)-ne.index(p[0])-1])+ ''.join(p)+ ''.join(s[len(ne)-ne.index(p[0])-1:]))
    else:
        air=''.join(s[0:s.index(p[0])])+''.join(p)+''.join(s[s.index(p[0]):])
        print(min(air,''.join(s[0:len(ne)-ne.index(p[0])-1])+ ''.join(p)+ ''.join(s[len(ne)-ne.index(p[0])-1:])))
    t-=1
