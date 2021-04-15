n=1
arr=list(map(int,input().split()))

def BinarySearchfirst(arr,l,r,n):
    #mid=(r+l)//2  #Normal or Brute Force approach

    mid=l+(r-l)//2 #Optimised to prevent integer overflow in case of 10^9 constraints.

    if r>=l:
        if (mid==0 or arr[mid]==n) and arr[mid-1]<n:
            return mid
        elif arr[mid]<n:
            return BinarySearchfirst(arr,mid+1,len(arr)-1,n)
        else:
            return BinarySearchfirst(arr,0,mid-1,n)
    else:
        return -1

low=0
high=1
while(n>arr[high]):
    low=high
    high=high*2
    
print(BinarySearchfirst(arr,low,high,n))
