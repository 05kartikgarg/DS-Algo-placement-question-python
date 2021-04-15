n=int(input())
arr=list(map(int,input().split()))


def BinarySearch(arr,l,r,n):
    #mid=(r+l)//2  #Normal or Brute Force approach

    mid=l+(r-l)//2 #Optimised to prevent integer overflow in case of 10^9 constraints.

    if arr[mid]==n:
        return mid
    elif arr[mid]>n:
        return BinarySearch(arr,0,mid-1,n)
    elif arr[mid]<n:
        return BinarySearch(arr,mid+1,len(arr)-1,n)
    else:
        return -1   

low=0
high=1
while(n>arr[high]):
    low=high
    high=high*2

print(BinarySearch(arr,low,high,n))
