'''
Row with max 1s 
Medium Accuracy: 42.51% Submissions: 12647 Points: 4
Given a boolean 2D array of n x m dimensions where each row is sorted. Find the 0-based index of the first row that has the maximum number of 1's.

Example 1:

Input: 
N = 4 , M = 4
Arr[][] = {{0, 1, 1, 1},
           {0, 0, 1, 1},
           {1, 1, 1, 1},
           {0, 0, 0, 0}}
Output: 2
Explanation: Row 2 contains 4 1's (0-based
indexing).

Example 2:

Input: 
N = 2, M = 2
Arr[][] = {{0, 0}, {1, 1}}
Output: 1
Explanation: Row 1 contains 2 1's (0-based
indexing).

Your Task:  
You don't need to read input or print anything. Your task is to complete the
function rowWithMax1s() which takes the array of booleans arr[][], n and m as
input parameters and returns the 0-based index of the first row that has the
most number of 1s. If no such row exists, return -1.
 

Expected Time Complexity: O(N+M)
Expected Auxiliary Space: O(1)
'''

def rowWithMax1s(self,arr, n, m):
	    ma=1000
	    r=-1
	    for i in range(n):
	        for j in range(m):
	            if arr[i][j]==1 and j<ma:
	                ma=j
	                r=i
	                break
	    return r
