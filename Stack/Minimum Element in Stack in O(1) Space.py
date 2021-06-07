stack=[]
me=-1

def getmin():
    if len(stack)==0:
        return -1
    return me

def push(x):
    if len(stack)==0:
        stack.append(x)
        me=x
    else:
        if x>=me:
            stack.append(x)
        elif x<me:
            stack.append(2*x-me)
            me=x

def popu():
    if len(stack)==0:
        return -1
    else:
        if stack[-1]>=me:
            stack.pop()
        elif stack[-1]<me:
            me=2*me-stack[-1]
            stack.pop()
def top():
    if len(stack)==0:
        return -1
    else:
        if stack[-1]>=me:
            return stack[-1]
        elif stack[-1]<me:
            return me
            
