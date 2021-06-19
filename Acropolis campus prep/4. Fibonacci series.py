n=int(input())
a=0
b=1
result=[a,b]
for i in range(2,n+1):
    c=a+b
    a=b
    b=c
    result.append(c)
print(result)
