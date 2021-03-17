'''
Chocolate Distribution Problem 

Given an array A of positive integers of size N, where each value represents number of
chocolates in a packet. Each packet can have variable number of chocolates. There are M
students, the task is to distribute chocolate packets such that :
1. Each student gets one packet.
2. The difference between the number of chocolates given to the students having packet
with maximum chocolates and student having packet with minimum chocolates is minimum.

Input:
The first line of input contains an integer T, denoting the number of test cases.
Then T test cases follow. Each test case consists of three lines. The first line of each test
case contains an integer N denoting the number of packets. Then next line contains N space
separated values of the array A denoting the values of each packet. The third line of each
test case contains an integer m denoting the no of students.

Output:
For each test case in a new line print the minimum difference.

Constraints:
1 <= T <= 100
1 <=N<= 107
1 <= Ai <= 1018
1 <= M <= N

Example:
Input:
2
8
3 4 1 9 56 7 9 12
5
7
7 3 2 4 9 12 56
3

Output:
6
2

Explanation:
Testcase 1: The minimum difference between maximum chocolates and minimum chocolates is 9-3=6
'''

def findMinDiff(arr, n, m):
 
    # if there are no chocolates or number
    # of students is 0
    if (m==0 or n==0):
        return 0
 
    # Sort the given packets
    arr.sort()
 
    # Number of students cannot be more than
    # number of packets
    if (n < m):
        return -1
 
    # Largest number of chocolates
    min_diff = arr[n-1] - arr[0]
 
    # Find the subarray of size m such that
    # difference between last (maximum in case
    # of sorted) and first (minimum in case of
    # sorted) elements of subarray is minimum.
    for i in range(len(arr) - m + 1):
        min_diff = min(min_diff ,  arr[i + m - 1] - arr[i])
     
         
    return min_diff
    
for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    m=int(input())
    print(findMinDiff(arr, n, m))
