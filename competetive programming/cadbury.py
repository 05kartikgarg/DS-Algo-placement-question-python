min_len=int(input())
max_len=int(input())
min_wid=int(input())
max_wid=int(input())
d={}
count=0

for l in range(min_len,max_len+1):
    for w in range(min_wid,max_wid+1):
        t_l=l
        t_w=w
        c=0
        if(t_l,t_w) in d:
            c=d[t_l,t_w]
        else:
            while(t_l!=0 or t_w!=0):
                if(t_l,t_w) in d:
                    c+=d[t_l,t_w]
                    break
                min_val=min(t_l,t_w)
                max_val=min(t_l,t_w)

                if(max_val%min_val==0):
                    c+=max_val/min_val
                    break
                else:
                    t_l=min_val
                    t_w=max_val-min_val
                    c+=1
            d[l,w]=c
            d[w,l]=c
        count+=c
print(int(count),end="")
            
