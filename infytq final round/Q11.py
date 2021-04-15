def fibonacci(n):
    l=[]
    num1=0
    num2=1
    l.append(num1)
    l.append(num2)
    while num2<n:
        s=num1+num2
        num1=num2
        num2=s
        l.append(num2)
    return l

arr=list(map(int,input().split()))
arr.sort()
max_num=arr[-1]
fib_list=fibonacci(max_num)
#print(fib_list)
fib_seq=[]
for i in range(len(arr)):
    if arr[i] in fib_list:
        fib_seq.append(arr[i])
if len(fib_seq)>2:
    print(len(fib_seq))
    #print(fib_seq)
else:
    print(-1)
