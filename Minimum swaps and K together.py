'''
Minimum swaps and K together 
Medium Accuracy: 36.68% Submissions: 2563 Points: 4
Given an array of n positive integers and a number k. Find the minimum number of swaps required to bring all the numbers less than or equal to k together.

Example 1:

â€‹Input : arr[ ] = {2, 1, 5, 6, 3} and K = 3
Output : 1
Explanation:
To bring elements 2, 1, 3 together, swap element '5' with '3'
such that final array will be- arr[] = {2, 1, 3, 6, 5}

â€‹Example 2:

Input : arr[ ] = {2, 7, 9, 5, 8, 7, 4} and K = 6 
Output :  2 
 

Your Task:
This is a function problem. The input is already taken care of by the driver code. You only need to complete the function minSwap() that takes an array (arr), sizeOfArray (n), an integer K, and return the minimum swaps required. The driver code takes care of the printing.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(1).
'''

# Python3 program to find 
# minimum swaps required 
# to club all elements less 
# than or equals to k together 

# Utility function to find 
# minimum swaps required to 
# club all elements less than 
# or equals to k together 
def minSwap(arr, n, k) : 
	
	# Find count of elements 
	# which are less than 
	# equals to k 
	count = 0
	for i in range(0, n) : 
		if (arr[i] <= k) : 
			count = count + 1
	
	# Find unwanted elements 
	# in current window of 
	# size 'count' 
	bad = 0
	for i in range(0, count) : 
		if (arr[i] > k) : 
			bad = bad + 1
	
	# Initialize answer with 
	# 'bad' value of current 
	# window 
	ans = bad 
	j = count 
	for i in range(0, n) : 
		
		if(j == n) : 
			break
			
		# Decrement count of 
		# previous window 
		if (arr[i] > k) : 
			bad = bad - 1
		
		# Increment count of 
		# current window 
		if (arr[j] > k) : 
			bad = bad + 1
		
		# Update ans if count 
		# of 'bad' is less in 
		# current window 
		ans = min(ans, bad) 

		j = j + 1

	return ans 

# Driver code 
arr = [2, 1, 5, 6, 3] 
n = len(arr) 
k = 3
print (minSwap(arr, n, k)) 

arr1 = [2, 7, 9, 5, 8, 7, 4] 
n = len(arr1) 
k = 5
print (minSwap(arr1, n, k)) 


