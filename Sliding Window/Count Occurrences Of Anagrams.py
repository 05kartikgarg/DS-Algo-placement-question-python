s=input()
pat=input()

def countocc(s,pat):
    n=len(s)
    k=len(pat)
    dic={}
    for i in pat:
        if i not in dic:
            dic[i]=1
        else:
            dic[i]+=1
    count=len(dic)
    ans=0
    i,j=0,0
    while j<n-1:
        if s[j] in dic:
            dic[s[j]]-=1
            if dic[s[j]]==0:
                count-=1
        if j-i+1<k:
            j+=1
        elif j-i+1==k:
            if count==0:
                ans+=1
            if s[i] in dic:
                dic[s[i]]-=1
            i+=1
            j+=1
            if s[j] in dic:
                if dic[s[j]]==0:
                    count+=1
                dic[s[j]]+=1
                
    return ans

print(countocc(s,pat))
                
                
            
