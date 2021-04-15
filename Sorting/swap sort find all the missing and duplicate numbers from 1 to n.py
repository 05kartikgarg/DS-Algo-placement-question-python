n=int(input())
arr=list(map(int,input().split()))

i=0

while(i<=n):
    if arr[i]!=arr[arr[i]-1]:
        arr[i],arr[arr[i]-1]=arr[arr[i]-1],arr[i]
    else:
        
        i+=1

for i in range(n):
    if arr[i]!=i+1:
        print("Missing= ",i+1,end=" ")
        print("Duplicate= ",arr[i],end=" ")
