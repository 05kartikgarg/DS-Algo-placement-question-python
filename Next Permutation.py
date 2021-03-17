'''
Next Permutation

Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such an arrangement is not possible, it must rearrange it as the lowest possible order (i.e., sorted in ascending order).

The replacement must be in place and use only constant extra memory.

 

Example 1:

Input: nums = [1,2,3]
Output: [1,3,2]
Example 2:

Input: nums = [3,2,1]
Output: [1,2,3]
Example 3:

Input: nums = [1,1,5]
Output: [1,5,1]
Example 4:

Input: nums = [1]
Output: [1]
 

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 100
'''
def nextPermutation(nums):
        def swap(a,b):
            nums[a],nums[b] = nums[b],nums[a]
            return
        def reverse(i):
            nums[i:] = nums[i:][::-1]
            
        if len(nums) <= 1:
            return 
        j = len(nums)-1
        while(j>=0 and nums[j-1] >= nums[j]):
            j-=1
        j-=1
        # Find the end of the non decreasing part of the array
        while(j>=0):
            i = j+1
            while(i<len(nums) and nums[j]<nums[i]):
                i+=1
            swap(i-1,j)
            #Swap with next greatest element on the right side
            break
        reverse(j+1)
        # Reverse the non increasing part
        return

l=list(map(int,input().split()))
