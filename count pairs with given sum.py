#count pairs with given sum

def getPairsCount(arr, n, k):
        count=0
        for i in range(n):
            diff=k-arr[i]
            if diff in arr and arr.index(diff)!=i:
                count+=arr.count(diff)
        return count//2

n,k=map(int,input().split())
arr=list(map(int,input().split()))
print(getPairsCount(arr, n, k))
