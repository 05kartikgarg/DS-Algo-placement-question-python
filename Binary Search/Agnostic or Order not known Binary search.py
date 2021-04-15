n=int(input())
arr=list(map(int,input().split()))
r=len(arr)-1

def BinarySearchAsc(arr,l,r,n):
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
    
def BinarySearchdesc(arr,l,r,n):
    #mid=(r+l)//2  #Normal or Brute Force approach

    mid=l+(r-l)//2 #Optimised to prevent integer overflow in case of 10^9 constraints.

    
    if arr[mid]==n:
        return mid
    elif arr[mid]>n:
        return BinarySearch(arr,mid+1,len(arr)-1,n)
    elif arr[mid]<n:
        return BinarySearch(arr,0,mid-1,n)
    else:
        return -1

if len(arr)==1:
    return arr[0]
else:
    if arr[0]<arr[1]:
        print(BinarySearchAsc(arr,0,r,n))
    else:
        print(BinarySearchdesc(arr,0,r,n))


              
