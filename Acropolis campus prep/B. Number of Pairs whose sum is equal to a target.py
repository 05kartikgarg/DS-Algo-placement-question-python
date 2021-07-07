n=int(input())
arr=list(map(int,input().split()))
target=int(input())

def getPairsCount(arr, n, sum):
    m = [0] * 1000
    
    for i in range(0, n):
        m[arr[i]] += 1
        
    twice_count = 0
    
    for i in range(0, n): 
        twice_count += m[sum - arr[i]]
        
        if (sum - arr[i] == arr[i]):
            twice_count -= 1
            
    return int(twice_count / 2)
 
print(getPairsCount(arr, n, target))
