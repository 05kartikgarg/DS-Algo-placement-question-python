n=int(input())
arr=list(map(int,input().split()))

mxl=[-1]*n
mxl[0]=arr[0]
for i in range(1,n):
    mxl[i]=max(mxl[i-1],arr[i])

mxr=[-1]*n
mxr[n-1]=arr[n-1]
for i in range(n-2,-1,-1):
    mxr[i]=max(mxr[i+1],arr[i])

water=[-1]*n
for i in range(n):
    water[i]=min(mxl[i],mxr[i])-arr[i]
ans=sum(water)
print(ans)

'''
n=6
arr=3 0 0 2 0 4
ans=10
'''
