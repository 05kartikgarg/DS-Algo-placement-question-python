a=int(input())
b=int(input())
mat1=[]
for i in range(a):
    temp=list(map(int,input().split()))
    mat1.append(temp)


c=int(input())
d=int(input())
mat2=[]
for i in range(c):
    temp=list(map(int,input().split()))
    mat2.append(temp)

result=[]
for i in range(a):
    temp=[0]*(d)
    result.append(temp)


if b!=c:
    print("Cannot be multiplied")
else:
    for i in range(a):
        for j in range(d):
            for k in range(c):
                result[i][j]+=mat1[i][k]*mat2[k][j]
    for p in result:
        print(" ".join(str(p)))
    

    
'''
3
3
12 7 3
4 5 6
7 8 9
3
3
5 8 1
6 7 3
4 5 9
'''
