import heapq
arr=list(map(int,input().split()))
dic={}
for i in arr:
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1

hp=[]
for i in dic:
    heapq.heappush(hp,(dic[i]*(-1),i))
            
while hp:
    print(heapq.heappop(hp)[1])
