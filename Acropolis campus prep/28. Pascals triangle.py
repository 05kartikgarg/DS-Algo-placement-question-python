def fact(n):
    if n==0 or n==1:
        return 1
    return n*fact(n-1)

def comb(n,r):
    if r==0 or n==0:
        return 1
    res=fact(n)//(fact(r)*fact(n-r))
    return res

n=int(input())
def generate(numRows):
        result=[]
        for i in range(numRows):
            temp=[]
            for j in range(i+1):
                temp.append(comb(i,j))
            result.append(temp)
        return result
l=generate(n)
for i in l:
    print(" ".join(str(i)))
        
