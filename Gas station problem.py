gas=list(map(int,input().split()))
cost=list(map(int,input().split()))

def canCompleteCircuit(gas,cost):
        summ=0
        start=0
        diff=0
        n=len(gas)
        for i in range(n):
            summ=summ+gas[i]-cost[i]
            if summ<0:
                start=i+1
                diff+=summ
                summ=0
        if summ+diff>=0:
            return start
        else:
            return -1

print(canCompleteCircuit(gas,cost))
