
arr=list(map(int,input().split()))
k=int(input())

def maxarray(arr,k):
    n=len(arr)
    i,j=0,0
    mx=[]
    ans=[]
    while j<n:
        while len(mx)>0 and mx[0]<arr[j]:
            mx.pop(0)
        mx.append(arr[j])
        if j-i+1<k:
            j+=1
        if j-i+1==k:
            ans.append(mx[0])
            if mx[0]==arr[i]:
                mx.pop(0)
            i+=1
            j+=1
    return ans

print(maxarray(arr,k))
            
'''
1 3 -1 -3 5 3 6 7
3
[3, 3, 5, 5, 6, 7]
'''
