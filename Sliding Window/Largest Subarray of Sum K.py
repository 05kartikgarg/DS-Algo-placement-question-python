arr=list(map(int,input().split()))
k=int(input())

def subarray(arr,k):
    n=len(arr)
    i,j=0,0
    s=0
    mx=0
    while j<n:
        s=s+arr[j]
        if s<k:
            j+=1
        elif s==k:
            mx=max(mx,j-i+1)
            j+=1
        elif s>k:
            while s>k:
                s=s-arr[i]
                i+=1
            j+=1
    return mx

print(subarray(arr,k))

'''
4 1 1 1 2 3 5
5
4
'''
            
