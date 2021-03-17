'''
Three way partitioning 

Given an array of size N and a range [a, b]. The task is to partition the array around the range such that array is divided into three parts.
1) All elements smaller than a come first.
2) All elements in range a to b come next.
3) All elements greater than b appear in the end.
The individual elements of three sets can appear in any order. You are required to return the modified array.


Example 1:

Input: 
N = 5
A[] = {1, 2, 3, 3, 4}
[a, b] = [1, 2]
Output: 1
Explanation: One possible arrangement is:
{1, 2, 3, 3, 4}. If you return a valid
arrangement, output will be 1.


Example 2:

Input: N = 3 
A[] = {1, 2, 3}
[a, b] = [1, 3]
Output: 1
Explanation: One possible arrangement 
is: {1, 2, 3}. If you return a valid
arrangement, output will be 1.


Your Task:
You dont need to read input or print anything. The task is to complete the function threeWayPartition() which takes the array[], a and b as input parameters and modifies the array in-place according to the given conditions.
Note: The generated output is 1 if you modify the given array successfully.


Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)
'''

# Python3 program to implement three way 
# partitioning around a given range. 

# Partitions arr[0..n-1] around [lowVal..highVal] 
def threeWayPartition(arr, n, lowVal, highVal): 

	# Initialize ext available positions for 
	# smaller (than range) and greater lements 
	start = 0
	end = n - 1
	i = 0

	# Traverse elements from left 
	while i <= end: 

		# If current element is smaller than 
		# range, put it on next available smaller 
		# position. 
		if arr[i] < lowVal: 
			temp = arr[i] 
			arr[i] = arr[start] 
			arr[start] = temp 
			i += 1
			start += 1

		# If current element is greater than 
		# range, put it on next available greater 
		# position. 
		elif arr[i] > highVal: 
			temp = arr[i] 
			arr[i] = arr[end] 
			arr[end] = temp 
			end -= 1

		else: 
			i += 1

# Driver code 
if __name__ == "__main__": 
	arr = [1, 14, 5, 20, 4, 2, 54, 
		20, 87, 98, 3, 1, 32] 
	n = len(arr) 

	threeWayPartition(arr, n, 10, 20) 

	print("Modified array") 
	for i in range(n): 
		print(arr[i], end = " ") 




