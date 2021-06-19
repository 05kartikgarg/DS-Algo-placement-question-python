def comb(n,r):
    if r==0:
        return 1
    res=(n-r+1)//r
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
print(generate(n))
        
