# same as the longest substring with k unique characters
s=input()
k=2

def longestsub(s,k):
    d={}
    n=len(s)
    ans=0
    i,j=0,0
    while j<n:
        if s[j] in d:
            d[s[j]]+=1
        else:
            d[s[j]]=1
        if len(d)<k:
            j+=1
        elif len(d)==k:
            ans=max(ans,j-i+1)
            j+=1
        elif len(d)>k:
            while len(d)>k:
                d[s[i]]-=1
                if d[s[i]]==0:
                    del d[s[i]]
                i+=1
            j+=1
    return ans

print(longestsub(s,k))

'''
abaccab
4
'''
            
