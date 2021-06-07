import heapq
arr=list(map(int,input().split()))
k=int(input())
s=list(set(arr))
hp=[]
for i in s:
    heapq.heappush(hp,(arr.count(i),i))
    if len(hp)>k:
        heapq.heappop(hp)
        
while hp:
    print(heapq.heappop(hp)[1])
