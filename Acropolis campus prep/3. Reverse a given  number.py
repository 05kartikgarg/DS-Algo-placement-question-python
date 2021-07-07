def reverse(s):
    temp=[i for i in s]
    n=len(temp)
    for i in range(n//2):
        temp[i],temp[n-i-1]=temp[n-i-1],temp[i]
    return "".join(temp)

n=int(input())
rev=reverse(str(n))
print(int(rev))

# Method 2

def reversed1(n):
    rev=0
    while n>0:
        rev=rev*10+n%10
        n=n//10
    return rev
print(reversed1(n))       
