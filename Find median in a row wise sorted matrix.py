'''
Median in a row-wise sorted Matrix 

Given a row wise sorted matrix of size RxC where R and C are always odd, find the median of
the matrix.

Example 1:

Input:
R = 3, C = 3
M = [[1, 3, 5], 
     [2, 6, 9], 
     [3, 6, 9]]

Output: 5

Explanation:
Sorting matrix elements gives us 
{1,2,3,3,5,6,6,9,9}. Hence, 5 is median. 
 

Example 2:

Input:
R = 3, C = 1
M = [[1], [2], [3]]
Output: 2

Your Task:  
You don't need to read input or print anything. Your task is to complete the function
median() which takes the integers R and C along with the 2D matrix as input parameters and
returns the median of the matrix.

Expected Time Complexity: O(32 * R * log(C))
Expected Auxiliary Space: O(1)
'''

def median(self, matrix, r, c):
    	if len(matrix)==1:
    	    vec=matrix[0]
    	    return vec[len(vec)//2]
    	else:
    	    new_list=[]
    	    for i in range(len(matrix)):
    	        new_list.extend(matrix[i])
    	    new_list.sort()
    	    if len(new_list)%2!=0:
    	        return new_list[len(new_list)//2]
    	    else:
    	        return(new_list[len(new_list)//2]+new_list[(len(new_list)//2)+1])//2
    	
