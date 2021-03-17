n=int(input())
arr=list(map(int,input().split()))

mxl=[-1]*(n)
mxr=[-1]*(n)

mxl[0]=arr[0]
for i in range(1,n):
    mxl[i]=max(mxl[i-1],arr[i])

mxr[n-1]=arr[n-1]
for i in range(n-2,-1,-1):
    mxr[i]=max(mxr[i+1],arr[i])

water=[]
for i in range(0,n):
    water.append(min(mxl[i],mxr[i])-arr[i])
print(sum(water))    

'''
n: 6
arr: 3 0 0 2 0 4
output: 10
'''
