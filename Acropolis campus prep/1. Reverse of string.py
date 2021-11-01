s=input()
temp=[i for i in s]
n=len(temp)
for i in range(n//2):
    temp[i],temp[n-i-1]=temp[n-i-1],temp[i]
print("".join(temp))
    
    
'''
s=input()
res=""
for i in s:
    res=i+res
print(res)

print("".join(reversed(s)))
'''
