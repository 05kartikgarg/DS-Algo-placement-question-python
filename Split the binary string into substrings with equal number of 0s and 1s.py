'''
Split the binary string into substrings with equal number of 0s and 1s

Given a binary string str of length N, the task is to find the maximum count of substrings str can be divided into such that all the substrings are balanced i.e. they have equal number of 0s and 1s. If it is not possible to split str satisfying the conditions then print -1.

Example:

Input: str = “0100110101”
Output: 4
The required substrings are “01”, “0011”, “01” and “01”.

Input: str = “0111100010”
Output: 3
'''

# Python3 implementation of the approach 

# Function to return the count 
# of maximum substrings str 
# can be divided into 
def maxSubStr(str, n): 
	
	# To store the count of 0s and 1s 
	count0 = 0
	count1 = 0
	
	# To store the count of maximum 
	# substrings str can be divided into 
	cnt = 0
	
	for i in range(n): 
		if str[i] == '0': 
			count0 += 1
		else: 
			count1 += 1
			
		if count0 == count1: 
			cnt += 1

# It is not possible to 
	# split the string 
	if count0 != count1: 
		return -1
			
	return cnt 

# Driver code 
str = "0100110101"
n = len(str) 
print(maxSubStr(str, n)) 
