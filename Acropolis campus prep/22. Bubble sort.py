def bubbleSort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j + 1] :
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

n=int(input())
arr=list(map(int,input().split()))
bubbleSort(arr)
print(arr)

'''
7
64 34 25 12 22 11 90
[11, 12, 22, 25, 34, 64, 90]
'''
