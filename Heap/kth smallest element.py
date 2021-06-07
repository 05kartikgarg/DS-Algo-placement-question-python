#For using it as a max heap multiply the elements of array with -1
import heapq
arr=list(map(int,input().split()))
k=int(input())
hp=[]
for i in arr:
    heapq.heappush(hp,i*(-1))
    if len(hp)>k:
        heapq.heappop(hp)
    
print((heapq.heappop(hp))*(-1))
