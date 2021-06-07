import heapq
arr=list(map(int,input().split()))
hp=[]
for i in arr:
    heapq.heappush(hp,i)
ans=0    
while len(hp)>1:
    r=heapq.heappop(hp)+heapq.heappop(hp)
    ans+=r
    heapq.heappush(hp,r)

print(ans)
