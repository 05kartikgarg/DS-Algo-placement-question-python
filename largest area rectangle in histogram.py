'''
Largest Rectangle in Histogram

Given n non-negative integers representing the histogram's bar height where the
width of each bar is 1, find the area of largest rectangle in the histogram.

Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].


The largest rectangle is shown in the shaded area, which has area = 10 unit.

 

Example:

Input: [2,1,5,6,2,3]
Output: 10
 

Example 1:

Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.

Example 2:

Input: heights = [2,4]
Output: 4
 

Constraints:

1 <= heights.length <= 105
0 <= heights[i] <= 104
'''

class Solution:
    def largestRectangleArea(self, ar: List[int]) -> int:
        n=len(ar)
		
		# next smaller right side
        def sr(ar,n):
            stack=[0]
            ans=[n] *n
            for i in range(1,n):
                while stack and ar[stack[-1]]>=ar[i]:
                    x=stack.pop()
                    ans[x]=i
                stack.append(i)
            return ans
			
        # next smaller left side
        def sl( ar,n):
            stack=[n-1]
            ans=[-1] *n
            for i in range(n-2,-1,-1):
                while stack and ar[stack[-1]]>ar[i]:
                    x=stack.pop()
                    ans[x]=i
                stack.append(i)
            return ans
        
			
        la=sl(ar,n)
        ra=sr(ar,n)
        width=[]

        for i in range(n):
            width.append(ra[i]-la[i]-1)
        ans=0

        for i in range(n):
            ans=max(ans,width[i]*ar[i])
        return ans
