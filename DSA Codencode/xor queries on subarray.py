arr=[1,3,4,8]
n=len(arr)
pre=[0]*(n)

pre[0]=arr[0]
for i in range(n):
    pre[i]=pre[i-1]^arr[i]
q=int(input())
while q>0:
    l,r=map(int,input().split())
    if l==0:
        print(pre[r])
    else:
        print(pre[r]^pre[l-1])
    q-=1
