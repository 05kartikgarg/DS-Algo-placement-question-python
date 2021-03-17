'''
Search a 2D Matrix

Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
 

Example 1:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
Example 2:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-104 <= matrix[i][j], target <= 104
'''
if not matrix or not matrix[0]:
            return False
        
        #finding out row
        for x in range(len(matrix)):
            
            if target == matrix[x][0] or target == matrix[x][-1]:
                return True
            
            elif target > matrix[x][0] and target < matrix[x][-1]:
                # look for element in row
                l, r = 0, len(matrix[x]) - 1
                
                while l <= r:
                    mid = l + (r - l) // 2
                    
                    if target == matrix[x][mid]:
                        return True
                    
                    elif target > matrix[x][mid]:
                        l = mid + 1
                        
                    else:
                        r = mid - 1
                        
                return False
