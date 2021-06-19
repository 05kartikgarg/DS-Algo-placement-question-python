n=int(input())
arr=list(map(int,input().split()))
r=len(arr)-1

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

print(BinarySearch(arr,0,r,n))   

'''
#Iterative

def BinarySearch(arr,l,r,n):
    while l<r:
        mid=l+(r-l)//2
        if arr[mid]==n:
            return mid
        elif arr[mid]>n:
            r=mid-1
        elif arr[mid]<n:
            l=mid+1
    return -1
'''
