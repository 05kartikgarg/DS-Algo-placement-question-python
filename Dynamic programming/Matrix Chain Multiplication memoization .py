'''
Given a sequence of matrices, find the most efficient way to multiply these matrices together.
The problem is not actually to perform the multiplications, but merely to decide in which
order to perform the multiplications.
We have many options to multiply a chain of matrices because matrix multiplication is
associative. In other words, no matter how we parenthesize the product, the result will be the
same. For example, if we had four matrices A, B, C, and D, we would have: 

(ABC)D = (AB)(CD) = A(BCD) = ....
However, the order in which we parenthesize the product affects the number of simple arithmetic
operations needed to compute the product, or the efficiency. For example, suppose A is a 10 ×30
matrix, B is a 30 × 5 matrix, and C is a 5 × 60 matrix. Then,  

(AB)C = (10×30×5) + (10×5×60) = 1500 + 3000 = 4500 operations
A(BC) = (30×5×60) + (10×30×60) = 9000 + 18000 = 27000 operations.
Clearly the first parenthesization requires less number of operations.
Given an array p[] which represents the chain of matrices such that the ith matrix Ai is of
dimension p[i-1] x p[i]. We need to write a function MatrixChainOrder() that should return the
minimum number of multiplications needed to multiply the chain. 

  
'''
#Bottom up approach
import sys
arr=list(map(int,input().split()))
i=1
j=len(arr)-1
dp=[[-1 for m in range(1001)]for n in range(1001)]
def solve(arr,i,j):
    if i>=j:
        return 0
    if dp[i][j]!=-1:
        return dp[i][j]
    mn=sys.maxsize
    for k in range(i,j):
        temp=solve(arr,i,k)+solve(arr,k+1,j)+(arr[i-1]*arr[k]*arr[j])
        if temp<mn:
            mn=temp
    dp[i][j]=mn
    return dp[i][j]
print(solve(arr,i,j))

'''
Input: p[] = {40, 20, 30, 10, 30}   
Output: 26000
There are 4 matrices of dimensions 40x20, 20x30, 30x10 and 10x30.
Let the input 4 matrices be A, B, C and D.  The minimum number of 
multiplications are obtained by putting parenthesis in following way
(A(BC))D --> 20*30*10 + 40*20*10 + 40*10*30
'''
