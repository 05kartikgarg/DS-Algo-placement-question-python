#For using it as a max heap multiply the elements of array with -1
import heapq
arr=list(map(int,input().split()))
k=int(input())
x=int(input())
hp=[]
for i in arr:
    heapq.heappush(hp,(abs(i-x)*(-1),i))
    if len(hp)>k:
        heapq.heappop(hp)
        
while hp:
    print(heapq.heappop(hp)[1])
