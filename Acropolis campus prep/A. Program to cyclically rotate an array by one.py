n=int(input())
arr=list(map(int,input().split()))

def rotate(arr,n):
    i=0
    j=n-1
    while i!=j:
        arr[i],arr[j]=arr[j],arr[i]
        i+=1
    return arr

print(rotate(arr,n))
