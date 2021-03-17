#Write a program to reverse an array or string

'''
Input  : arr[] = {1, 2, 3}
Output : arr[] = {3, 2, 1}

Input :  arr[] = {4, 5, 1, 2}
Output : arr[] = {2, 1, 5, 4}

'''
n=int(input())
l=list(map(int, input().split()))
for i in range(n-1,-1,-1):
    print(l[i],end=' ')
