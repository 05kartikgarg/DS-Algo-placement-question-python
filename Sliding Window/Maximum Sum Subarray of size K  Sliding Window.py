'''
Given an array of integers and a number k, find maximum sum of a subarray of size k.

Examples :

Input  : arr[] = {100, 200, 300, 400}
         k = 2
Output : 700

Input  : arr[] = {1, 4, 2, 10, 23, 3, 1, 0, 20}
         k = 4 
Output : 39
We get maximum sum by adding subarray {4, 2, 10, 23}
of size 4.

Input  : arr[] = {2, 3}
         k = 3
Output : Invalid
There is no subarray of size 3 as size of whole
array is 2.

'''

# O(n) solution in Python3 for finding 
# maximum sum of a subarray of size k 

# Returns maximum sum in 
# a subarray of size k. 
def maxSum(arr, n, k): 

	# k must be greater 
	if (n < k): 
	
		print("Invalid") 
		return -1
	
	# Compute sum of first 
	# window of size k 
	res = 0
	for i in range(k): 
		res += arr[i] 

	# Compute sums of remaining windows by 
	# removing first element of previous 
	# window and adding last element of 
	# current window. 
	curr_sum = res 
	for i in range(k, n): 
	
		curr_sum += arr[i] - arr[i-k] 
		res = max(res, curr_sum) 

	return res 

# Driver code 
arr = [1, 4, 2, 10, 2, 3, 1, 0, 20] 
k = 4
n = len(arr) 
print(maxSum(arr, n, k)) 

 
