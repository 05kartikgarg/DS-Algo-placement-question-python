n=int(input())
num=list(map(int,input().split()))
lis_count=[]
uniq=set(num)
for i in uniq:
    count=num.count(i)
    lis_count.append(count)
lis_count.sort()
l=len(lis_count)
for c in lis_count:
    if c<=n:
        n-=c
        l-=1
    else:
        break
print(l)

'''
n: 4
arr: 1 1 1 2 2 3 3 4 5 6
output: 3
'''
