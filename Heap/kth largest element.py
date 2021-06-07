import heapq
arr=list(map(int,input().split()))
k=int(input())
hp=[]
for i in arr:
    heapq.heappush(hp,i)
    if len(hp)>k:
        heapq.heappop(hp)
        #print(hp)
print(heapq.heappop(hp))
