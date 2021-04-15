arr=list(map(int,input().split()))

low=0
high=len(arr)-1
result=-1
while(low<=high):
    mid=low+(high-low)//2

    if(mid>0 and mid<len(arr)-1):
        if((arr[mid]>arr[mid-1])and(arr[mid]>arr[mid+1])):
            result=mid
            break
        elif arr[mid-1]>arr[mid]:
            high=mid-1
        else:
            low=mid+1
            
    elif mid==0:
        if arr[0]>arr[1]:
            result=0
            break
        else:
            result=1
            break
            
    elif mid==len(arr)-1:
        if arr[len(arr)-1]>arr[len(arr)-2]:
            result=len(arr)-1
            break
        else:
            result=len(arr)-2
            break
print(result)
        
