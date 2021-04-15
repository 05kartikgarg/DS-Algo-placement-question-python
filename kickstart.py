for t in range(int(input())):
    n,k=map(int,input().split())
    s=input()
    temp1=[s[i] for i in range(n//2)]
    temp2=[s[i] for i in range(n//2,n)]
    score=0
    t2=len(temp2)
    for i in range(len(temp1)):
        #print(temp1[i],temp2[t2-i-1])
        if temp1[i]!=temp2[t2-i-1]:
            score+=1
                
    
    print(score)
    r=k-score
    print("case #"+str(t+1)+":",r)

    
