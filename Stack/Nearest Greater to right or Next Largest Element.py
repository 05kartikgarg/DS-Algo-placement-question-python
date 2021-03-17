from collections import deque
arr=list(map(int,input().split()))

def NGR(arr):
    stack=deque()
    result=[]
    for i in range(len(arr)-1,-1,-1):
        if len(stack)==0:
            result.append(-1)
        elif len(stack)>0 and stack[-1]>arr[i]:
            result.append(stack[-1])
        elif len(stack)>0 and stack[-1]<=arr[i]:
            while len(stack)>0 and stack[-1]<=arr[i]:
                stack.pop()
            if len(stack)==0:
                result.append(-1)
            else:
                result.append(stack[-1])
        stack.append(arr[i])
    for i in range(-1,-len(result)-1,-1):
        print(result[i],end=' ')

NGR(arr)
