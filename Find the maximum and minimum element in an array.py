#Maximum and minimum of an array using minimum number of comparisons

'''
#Method 1

l=list(map(int, input().split()))
maximum=max(l)
minimum=min(l)
print("Maximum=",maximum)
print("Minimum=",minimum)

'''
#Method 2

l=list(map(int, input().split()))
maxi=l[0]
mini=l[0]

for i in l:
    if i>maxi:
        maxi=i
    if i<mini:
        mini=i
print("Maximum=",maxi)
print("Minimum=",mini)

