arr=list(map(int,input().split(',')))
n=len(arr)

def rearrange(arr, n):
    j = 0
    for i in range(0, n):
        if (arr[i] < 0):
            temp = arr[i]
            arr[i] = arr[j]
            arr[j]= temp
            j = j + 1
    return arr
print(rearrange(arr, n))