n=int(input())
m=int(input())
key=int(input())
arr=list()
for i in range(n):
    temp=list(map(int,input().split()))
    arr.append(temp)
i,j=0,m-1

while(i>=0 and i<n and j>=0 and j<m):
    if arr[i][j]==key:
        res=(i,j)
        break
    elif arr[i][j]>key:
        j-=1
    elif arr[i][j]<key:
        i+=1
    else:res=-1
print(res)
    
