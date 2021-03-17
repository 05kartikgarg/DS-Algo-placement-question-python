arr=list(map(int,input().split()))

def NGL(arr):
    stack=[[]]
    result=[]
    for i in range(len(arr)):
        if len(stack[-1])==0:
            result.append(-1)
            
        elif len(stack)>0 and stack[-1][0]>arr[i]:
            result.append(stack[-1][1])
            
        elif len(stack)>0 and stack[-1][0]<=arr[i]:
            while len(stack)>0 and stack[-1][0]<=arr[i]:
                stack.pop()
            if len(stack)==0:
                result.append(-1)
            else:
                result.append(stack[-1][1])
        stack.append([arr[i],i])
        
        
    for i in range(len(arr)):
        print(i-result[i],end=' ')

NGL(arr)
