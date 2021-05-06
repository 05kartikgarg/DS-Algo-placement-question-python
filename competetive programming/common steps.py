'''
#method 1: Recursion
def ways(n):
    if n==1 or n==0:
        return 1
    elif n==2:
        return 2
    else:
        return ways(n-3)+ways(n-2)+ways(n-1)

n=int(input())
print(ways(n))
'''

#method 2: Dynamic approach

n=int(input())
ways=[]
ways=[0]*(n+1)
ways[0]=1
ways[1]=1
ways[2]=2

for i in range(3,n+1):
    ways[i]=ways[i-3]+ways[i-2]+ways[i-1]

print(ways[n])
