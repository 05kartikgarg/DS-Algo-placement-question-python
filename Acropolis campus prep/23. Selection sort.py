def selectionsort(A):
    for i in range(len(A)):
        min_idx = i
        for j in range(i+1, len(A)):
            if A[min_idx] > A[j]:
                min_idx = j      
        A[i], A[min_idx] = A[min_idx], A[i]

n=int(input())
A=list(map(int,input().split()))
selectionsort(A)
print(" ".join(str(i) for i in A))

'''
7
64 34 25 12 22 11 90
[11, 12, 22, 25, 34, 64, 90]
'''
