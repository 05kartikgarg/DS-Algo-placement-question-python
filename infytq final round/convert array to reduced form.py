'''
for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    temp=arr.copy()
    temp.sort()
    for i in range(len(arr)):
        arr[i]=temp.index(arr[i])
    print(arr)
'''

'''
for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    for i in arr:
        if arr.count(i)>n//2:
            print(i)
            break
        else:
            print(-1)
'''
