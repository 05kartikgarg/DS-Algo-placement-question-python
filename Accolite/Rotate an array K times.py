'''
def rotate(self, nums: List[int], k: int) -> None:
        
        n=len(nums)
        k=k%n
        nums.reverse()
        nums[0:k]=reversed(nums[0:k])
        nums[k:]=reversed(nums[k:])

'''

arr=list(map(int,input().split()))
n=len(arr)
k=int(input())

def rotate(arr,n):
        i=0
        j=n-1
        while i!=j:
                arr[i],arr[j]=arr[j],arr[i]
                i+=1
        
while k!=0:
        rotate(arr,n)
        k-=1
print(" ".join([str(i) for i in arr]))
