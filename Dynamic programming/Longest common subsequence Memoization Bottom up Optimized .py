'''
Given a string, a partitioning of the string is a palindrome partitioning if every substring
of the partition is a palindrome. For example, “aba|b|bbabb|a|b|aba” is a palindrome partitioning
of “ababbbabbababa”. Determine the fewest cuts needed for a palindrome partitioning of a given
string. For example, minimum of 3 cuts are needed for “ababbbabbababa”. The three cuts are
“a|babbbab|b|ababa”. If a string is a palindrome, then minimum 0 cuts are needed. If a string
of length n containing all different characters, then minimum n-1 cuts are needed. 
'''
import sys
s=input()
i,j=0,len(s)-1
dp=[[-1 for m in range(1001)]for n in range(1001)]
def ispalindrome(s,i,j):
    if i==j:
        return True
    if i>j:
        return True
    while i<j:
        if s[i]!=s[j]:
            return False
        i+=1
        j-=1
    return True
def solve(s,i,j):
    if i>=j:
        return 0
    if (ispalindrome(s,i,j)==True):
        return 0
    if dp[i][j]!=-1:
        return dp[i][j]
    mn=sys.maxsize
    for k in range(i,j):
        if dp[i][k]!=-1:
            left=dp[i][k]
        else:
            left=solve(s,i,k)

        if dp[k+1][j]!=-1:
            right=dp[k+1][j]
        else:
            right=solve(s,k+1,j)
            
        temp=1+left+right
        if temp<mn:
            mn=temp
        dp[i][j]=mn
    return dp[i][j]

print(solve(s,i,j))

'''
Input : str = “geek” 
Output : 2 
'''
