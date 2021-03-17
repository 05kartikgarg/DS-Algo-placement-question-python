#Kadane's algo to find max sum in a contiguous sub array

# https://practice.geeksforgeeks.org/problems/kadanes-algorithm-1587115620/1#

n=int(input())
arr=list(map(int,input().split()))

max_so_far = 0
max_ending_here = 0
    
for i in range(0, n):
    max_ending_here = max_ending_here + arr[i]
    if max_ending_here < arr[i]:
        max_ending_here = arr[i]
        
    if (max_so_far < max_ending_here):
        max_so_far = max_ending_here
print(max_so_far)
