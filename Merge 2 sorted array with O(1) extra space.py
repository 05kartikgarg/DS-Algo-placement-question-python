'''
Given two sorted arrays arr1[] of size N and
arr2[] of size M. Each array is sorted in
non-decreasing order. Merge the two arrays into
one sorted array in non-decreasing order without
using any extra space

Example 1:

Input:
N = 4, M = 5
arr1[] = {1, 3, 5, 7}
arr2[] = {0, 2, 6, 8, 9}
Output: 0 1 2 3 5 6 7 8 9
Explanation: Since you can't use any 
extra space, modify the given arrays
to form 
arr1[] = {0, 1, 2, 3}
arr2[] = {5, 6, 7, 8, 9}

'''
n,m=map(int, input().split())
a=list(map(int, input().split()))
b=list(map(int, input().split()))

i,j=n-1,0

while i>=0 and j<m:
    if a[i]>b[j]:
        a[i],b[j]=b[j],a[i]
    i-=1
    j+=1
a.sort()
b.sort()
print(a)
print(b)
        
'''
Time Complexity: O((n+m)*log(n+m))
Auxiliary Space: O(1)
'''
    
