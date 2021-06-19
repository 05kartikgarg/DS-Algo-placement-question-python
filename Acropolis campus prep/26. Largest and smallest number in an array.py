n=int(input())
arr=list(map(int,input().split()))

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
7
64 34 25 12 22 11 90
90
11

'''
