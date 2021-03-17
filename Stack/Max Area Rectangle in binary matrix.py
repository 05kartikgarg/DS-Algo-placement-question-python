n,m=map(int,input().split())
arr=[]
for i in range(n):
    t=list(map(int,input().split()))
    arr.append(t)

def MAH(arr):
    def NSL(arr):
        stack=[[]]
        result=[]
        for i in range(len(arr)):
            if len(stack[-1])==0:
                result.append(-1)
                
            elif len(stack)>0 and stack[-1][0]<arr[i]:
                result.append(stack[-1][1])
                
            elif len(stack)>1 and stack[-1][0]>=arr[i]:
                while len(stack)>1 and stack[-1][0]>=arr[i]:
                    stack.pop()
                    
                if len(stack)==1:
                    result.append(-1)
                else:
                    result.append(stack[-1][1])
            stack.append([arr[i],i])
        
        return result

    def NSR(arr):
        stack=[[]]
        result=[]
        pseudo_ind=len(arr)
        for i in range(len(arr)-1,-1,-1):
            if len(stack[-1])==0:
                result.append(pseudo_ind)
            elif len(stack)>0 and stack[-1][0]<arr[i]:
                result.append(stack[-1][1])
            elif len(stack)>1 and stack[-1][0]>=arr[i]:
                while len(stack)>1 and stack[-1][0]>=arr[i]:
                    stack.pop()
                if len(stack)==1:
                    result.append(pseudo_ind)
                else:
                    result.append(stack[-1][1])
            stack.append([arr[i],i])
        result.reverse()
        return result

    left=NSL(arr)
    right=NSR(arr)
    width=[]
    area=[]
    for i in range(len(arr)):
        width.append(right[i]-left[i]-1)
        
    for i in range(len(arr)):
        area.append(arr[i]*width[i])


    return max(area)

v=[]
for j in range(0,m):
    v.append(arr[0][j])
mx=MAH(v)

for i in range(1,n):
    for j in range(0,m):
        if arr[i][j]==0:
            v[j]=0
        else:
            v[j]+=arr[i][j]
    mx=max(mx,MAH(v))

print(mx)


'''
n,m=4,4
arr:0 1 1 0
    1 1 1 1
    1 1 1 1
    1 1 0 0
    
output: 8
'''
