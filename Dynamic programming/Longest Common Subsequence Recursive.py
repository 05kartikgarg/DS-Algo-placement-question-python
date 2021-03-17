m,n=map(int,input().split())
x=input()
y=input()

def LCS(x,y,m,n):
    if m==0 or n==0:
        return 0

    if x[m-1]==y[n-1]:
        return 1 + LCS(x,y,m-1,n-1)
    else:
        return max(LCS(x,y,m-1,n),LCS(x,y,m,n-1))
    
print(LCS(x,y,m,n))

'''
m,n=6,6
x=ABCDGH
y=AEDFHR

OUTPUT: 3
'''
