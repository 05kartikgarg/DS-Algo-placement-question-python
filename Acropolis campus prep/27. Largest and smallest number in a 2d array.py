m=int(input())
n=int(input())
mat=[]
arr=[]
for i in range(m):
    temp=list(map(int,input().split()))
    mat.append(temp)
for i in mat:
    arr.extend(i)

maximum=arr[0]
minimum=arr[0]
for i in range(1,n):
    if maximum<arr[i]:
        maximum=arr[i]
    if minimum>arr[i]:
        minimum=arr[i]
print("maximum ",maximum)
print("minimum ",minimum)

'''
3
3
5 8 1
4 2 6
7 4 3
maximum  8
minimum  1
'''
