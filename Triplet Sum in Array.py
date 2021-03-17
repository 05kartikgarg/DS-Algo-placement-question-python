'''
Triplet Sum in Array 

Given an array arr of size N and an integer K. Find if there's a triplet in the
array which sums up to the given integer K.

Example 1:

Input:
N = 6, K = 13
arr[] = [1 4 45 6 10 8]
Output:
true
Explanation:
The triplet {1, 4, 8} in 
the array sums up to 13.
Example 2:

Input:
N = 5, K = 10
arr[] = [1 2 4 3 6]
Output:
true
Explanation:
The triplet {1, 3, 6} in 
the array sums up to 10.

Your Task:
You don't need to read input or print anything. Your task is to complete the
function find3Numbers() which takes the array arr[], the size of the array (N)
and the sum (X) as inputs and returns True if there exists a triplet in the
array arr[] which sums up to X and False otherwise.

Expected Time Complexity: O(N2)
Expected Auxiliary Space: O(1)

Constraints:
1 ≤ N ≤ 103
1 ≤ A[i] ≤ 105
'''

# Python3 program to find a triplet

# returns true if there is triplet
# with sum equal to 'sum' present
# in A[]. Also, prints the triplet
def find3Numbers(A, arr_size, sum):

    # Sort the elements 
    A.sort()

    # Now fix the first element 
    # one by one and find the
    # other two elements 
    for i in range(0, arr_size-2):
    

        # To find the other two elements,
        # start two index variables from
        # two corners of the array and
        # move them toward each other
        
        # index of the first element
        # in the remaining elements
        l = i + 1 
        
        # index of the last element
        r = arr_size-1 
        while (l < r):
        
            if( A[i] + A[l] + A[r] == sum):
                print("Triplet is", A[i], 
                     ', ', A[l], ', ', A[r]);
                return True
            
            elif (A[i] + A[l] + A[r] < sum):
                l += 1
            else: # A[i] + A[l] + A[r] > sum
                r -= 1

    # If we reach here, then
    # no triplet was found
    return False

# Driver program to test above function 
A = [1, 4, 45, 6, 10, 8]
sum = 22
arr_size = len(A)

find3Numbers(A, arr_size, sum)
