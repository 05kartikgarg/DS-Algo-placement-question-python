n=int(input())
arr=list(map(int,input().split()))
r=len(arr)-1

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

print("First Occurence of "+str(n)+" = ",BinarySearchfirst(arr,0,r,n))

def BinarySearchlast(arr,l,r,n):
    #mid=(r+l)//2  #Normal or Brute Force approach

    mid=l+(r-l)//2 #Optimised to prevent integer overflow in case of 10^9 constraints.

    if r>=l:
        if (mid==len(arr)-1 or arr[mid]==n) and arr[mid+1]>n:
            return mid
        elif arr[mid]>n:
            return BinarySearchlast(arr,0,mid-1,n)
        else:
            return BinarySearchlast(arr,mid+1,len(arr)-1,n)
    else:
        return -1  

print("Last Occurence of "+str(n)+" = ",BinarySearchlast(arr,0,r,n))
