n=int(input())
arr=list(map(int,input().split()))
r=len(arr)-1

def BinarySearch(arr,l,r,n):
    #mid=(r+l)//2  #Normal or Brute Force approach

    mid=l+(r-l)//2 #Optimised to prevent integer overflow in case of 10^9 constraints.

    
    if arr[mid]==n:
        return mid
    if mid>l and arr[mid-1]==n:
        return mid-1
    if mid<r and arr[mid+1]==n:
        return mid+1
    
    if arr[mid]>n:
        return BinarySearch(arr,0,mid-2,n)
    elif arr[mid]<n:
        return BinarySearch(arr,mid+2,len(arr)-1,n)
    else:
        return -1

print(BinarySearch(arr,0,r,n))   
