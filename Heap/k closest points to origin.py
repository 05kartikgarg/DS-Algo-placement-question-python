import heapq
n=int(input())
arr=[]
for i in range(n):
    x,y=map(int,input().split())
    arr.append((x,y))
k=int(input())
hp=[]

for i in arr:
    value=i[0]*i[0]+i[1]*i[1]
    heapq.heappush(hp,(value*(-1),i))
    if len(hp)>k:
        heapq.heappop(hp)
            
while hp:
    print(heapq.heappop(hp)[1])

'''
4
1 3
-2 2
5 8
0 1
2
'''
