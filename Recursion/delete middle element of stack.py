stack=list(map(int,input().split()))
k=(len(stack))//2 + 1

def solve(stack,k):
    if k==1:
        stack.pop()
        return
    temp=stack[len(stack)-1]
    stack.pop()
    solve(stack,k-1)
    stack.append(temp)
    return
if len(stack)==0:
    print(' '.join(stack))
else:
    r=solve(stack,k)
    print(r)
