stack=[]
ss=[]

def push(a):
    stack.append(a)
    if len(ss)==0 or ss[-1]>=a:
        ss.append(a)
    return

def popu():
    if len(ss)==0:
        return -1
    ans=stack.pop()
    if ss[-1]==ans:
        ss.pop()
    return ans

def getmin():
    if len(ss)==0:
        return -1
    return ss[-1]
