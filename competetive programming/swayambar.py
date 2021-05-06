n=int(input())
bride=input()
groom=input()
gr=0
gm=0
for g in groom:
    if(g=='r'):
        gr+=1
    else:
        gm+=1
count=0

for b in bride:
    if(b=='r'):
        if(gr>0):
            gr-=1
            count+=1
        else:
            break
    else:
        if(gm>0):
            gm-=1
            count+=1
        else:
            break

print(n-count,end='')
