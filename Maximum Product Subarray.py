'''
Maximum Product Subarray 
Given an array Arr that contains N integers (may be positive, negative or zero). Find the product of the maximum product subarray.

Example 1:

Input:
N = 5
Arr[] = {6, -3, -10, 0, 2}
Output: 180
Explanation: Subarray with maximum product
is  6, -3, -10 which gives product as 180.
Example 2:

Input:
N = 6
Arr[] = {2, 3, 4, 5, -1, 0}
Output: 120
Explanation: Subarray with maximum product
is 2, 3, 4, 5 which gives product as 120.
Your Task:
You don't need to read input or print anything. Your task is to complete the function maxProduct() which takes the array of integers arr and n as parameters and returns an integer denoting the answer.
Note: Use 64-bit integer data type to avoid overflow.

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)

Constraints:
1 <= N <= 500
-102 <= Arri <= 102
'''
# Python 3 program to find maximum 
# product subarray 

# Function to find maximum 
# product subarray 
def maxProduct(arr, n): 
	
	# Variables to store maximum and 
	# minimum product till ith index. 
	minVal = arr[0] 
	maxVal = arr[0] 

	maxProduct = arr[0] 

	for i in range(1, n, 1): 
		
		# When multiplied by -ve number, 
		# maxVal becomes minVal 
		# and minVal becomes maxVal. 
		if (arr[i] < 0): 
			temp = maxVal 
			maxVal = minVal 
			minVal = temp 
			
		# maxVal and minVal stores the 
		# product of subarray ending at arr[i]. 
		maxVal = max(arr[i], maxVal * arr[i]) 
		minVal = min(arr[i], minVal * arr[i]) 

		# Max Product of array. 
		maxProduct = max(maxProduct, maxVal) 

	# Return maximum product 
	# found in array. 
	return maxProduct 

# Driver Code 
if __name__ == '__main__': 
	arr = [-1, -3, -10, 0, 60] 

	n = len(arr) 

	print("Maximum Subarray product is", 
					maxProduct(arr, n)) 


