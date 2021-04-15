n=int(input())
arr=list(map(int,input().split()))
k=int(input())

def isvalid(arr,n,k,mx):
    student=1
    s=0
    for i in range(n):
        s+=arr[i]
        if s>mx:
            student+=1
            s=arr[i]
    if student>k:
        return False
    else:
        return True

if n<k:
    print(-1)
else:
    start=max(arr)
    end=sum(arr)
    res=-1

    while(start<=end):
        mid=start+(end-start)//2

        if(isvalid(arr,n,k,mid)==True):
            res=mid
            end=mid-1
        else:
            start=mid+1
    print(res)

