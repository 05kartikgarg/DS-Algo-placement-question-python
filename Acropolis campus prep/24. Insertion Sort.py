def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key

n=int(input())
arr=list(map(int,input().split()))
insertionSort(arr)
print(arr)

'''
7
64 34 25 12 22 11 90
[11, 12, 22, 25, 34, 64, 90]
'''
