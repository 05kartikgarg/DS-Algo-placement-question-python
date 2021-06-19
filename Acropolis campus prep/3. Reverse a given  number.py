def reverse(s):
    temp=[i for i in s]
    n=len(temp)
    for i in range(n//2):
        temp[i],temp[n-i-1]=temp[n-i-1],temp[i]
    return "".join(temp)

n=int(input())
rev=reverse(str(n))
print(int(rev))

