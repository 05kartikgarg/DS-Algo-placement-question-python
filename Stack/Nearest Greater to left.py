from collections import deque
arr=list(map(int,input().split()))

def NGL(arr):
    stack=deque()
    result=[]
    for i in range(len(arr)):
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
    for i in range(len(arr)):
        print(result[i],end=' ')

NGL(arr)
