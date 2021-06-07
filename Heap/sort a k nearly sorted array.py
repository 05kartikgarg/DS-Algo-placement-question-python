import heapq
arr=list(map(int,input().split()))
k=int(input())
hp=[]
res=[]

for i in arr:
    heapq.heappush(hp,i)
    if len(hp)==k:
        res.append(heapq.heappop(hp))

res.extend(hp)    
print(res)
