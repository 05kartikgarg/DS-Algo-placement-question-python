'''
Smallest subarray with sum greater than x 
Easy Accuracy: 44.8% Submissions: 2761 Points: 2
Given an array of integers (A[])  and a number x, find the smallest subarray with sum greater than the given value.

Note: The answer always exists. It is guaranteed that x doesn't exceed the summation of a[i] (from 1 to N).

Example 1:

Input:
A[] = {1, 4, 45, 6, 0, 19}
x  =  51
Output: 3
Explanation:
Minimum length subarray is 
{4, 45, 6}

Example 2:
Input:
A[] = {1, 10, 5, 2, 7}
   x  = 9
Output: 1
Explanation:
Minimum length subarray is {10}
 

Your Task:  
You don't need to read input or print anything. Your task is to complete the function sb() which takes the array A[], its size N and an integer X as inputs and returns the required ouput.


Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)
'''

# O(n) solution for finding smallest
# subarray with sum greater than x

# Returns length of smallest subarray
# with sum greater than x. If there
# is no subarray with given sum, then
# returns n + 1


def smallestSubWithSum(arr, n, x):

	# Initialize current sum and minimum length
	curr_sum = 0
	min_len = n + 1

	# Initialize starting and ending indexes
	start = 0
	end = 0
	while (end < n):

		# Keep adding array elements while current
		# sum is smaller than or equal to x
		while (curr_sum <= x and end < n):
			curr_sum += arr[end]
			end += 1

		# If current sum becomes greater than x.
		while (curr_sum > x and start < n):

			# Update minimum length if needed
			if (end - start < min_len):
				min_len = end - start

			# remove starting elements
			curr_sum -= arr[start]
			start += 1

	return min_len


# Driver program
arr1 = [1, 4, 45, 6, 10, 19]
x = 51
n1 = len(arr1)
res1 = smallestSubWithSum(arr1, n1, x)
print("Not possible") if (res1 == n1 + 1) else print(res1)

arr2 = [1, 10, 5, 2, 7]
n2 = len(arr2)
x = 9
res2 = smallestSubWithSum(arr2, n2, x)
print("Not possible") if (res2 == n2 + 1) else print(res2)

arr3 = [1, 11, 100, 1, 0, 200, 3, 2, 1, 250]
n3 = len(arr3)
x = 280
res3 = smallestSubWithSum(arr3, n3, x)
print("Not possible") if (res3 == n3 + 1) else print(res3)






