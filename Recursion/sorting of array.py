#some thing is incorrect

def insert(arr,temp):
    if len(arr)==0 or arr[-1]<=temp:
        arr.append(temp)
    val=arr[-1]
    arr.pop()
    insert(arr,temp)
    arr.append(val)
    return arr


def sort(arr):
    if len(arr)==0:
        return arr
    temp=arr[-1]
    arr.pop()
    sort(arr)
    insert(arr,temp)

arr=list(map(int,input().split()))
sort(arr)
print(arr)