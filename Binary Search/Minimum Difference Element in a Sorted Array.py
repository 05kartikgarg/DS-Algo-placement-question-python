n=int(input())
arr=list(map(int,input().split()))

low=0
high=len(arr)-1
res=-1
while low<=high:
    mid=low+(high-low)//2
    
    if n==arr[mid]:
        res=arr[mid]
    elif n<arr[mid]:
        high=mid-1
    else:
        low=mid+1

min1=abs(arr[low]-n)
min2=abs(arr[high]-n)

if min1<min2:
    res=min1
else:
    res=min2

print(res)
        
