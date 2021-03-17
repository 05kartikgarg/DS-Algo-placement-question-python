x=input()
y=input()
m,n=len(x),len(y)
dp=[[-1 for i in range(1001)] for j in range(1001)]
def LCS(x,y,m,n):
    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j==0:
                dp[i][j]=0
    for i in range(1,m+1):
        for j in range(1,n+1):
            if x[i-1]==y[j-1]:
                dp[i][j]= 1 + dp[i-1][j-1]
                
            else:
                dp[i][j]= max(dp[i-1][j],dp[i][j-1])
    return dp[m][n]
LCS(x,y,m,n)

i,j=m,n
string=''
while i>0 and j>0:
    if x[i-1]==y[j-1]:
        string+=x[i-1]
        i-=1
        j-=1
    else:
        if dp[i][j-1]>dp[i-1][j]:
            string+=y[j-1]
            j-=1
        else:
            string+=x[i-1]
            i-=1
while i>0:
    string+=x[i-1]
    i-=1
    
while j>0:
    string+=y[j-1]
    j-=1
print(string[-1:-len(string)-1:-1])

'''

X = "HELLO",  Y = "GEEK"
Output: "GEHEKLLO" OR "GHEEKLLO"
'''
