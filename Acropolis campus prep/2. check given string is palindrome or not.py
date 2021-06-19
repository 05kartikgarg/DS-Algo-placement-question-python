s=input()
temp=[i for i in s]
n=len(temp)
flag=1
for i in range(n//2+1):
    if temp[i]!=temp[n-i-1]:
        flag=0
        break

if flag==0:
    print("False")
else:
    print("True")
