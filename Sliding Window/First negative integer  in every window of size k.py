# Python3 code for First negative integer 
# in every window of size k
'''
def printFirstNegativeInteger(arr, k):
	firstNegativeIndex = 0

	for i in range(k - 1, len(arr)):

		# skip out of window and positive elements
		while firstNegativeIndex < i and (firstNegativeIndex <= i - k or arr[firstNegativeIndex] > 0):
			firstNegativeIndex += 1

		# check if a negative element is found, otherwise use 0
		firstNegativeElement = arr[firstNegativeIndex] if arr[firstNegativeIndex] < 0 else 0
		print(firstNegativeElement, end=' ')


if __name__ == "__main__":
	arr = [12, -1, -7, 8, -15, 30, 16, 28]
	k = 3
	printFirstNegativeInteger(arr, k)
'''

def firstnegative(arr,k):
        i,j=0,0
        neg=[]
        res=[]
        while j<len(arr):
                if arr[j]<0:
                        neg.append(arr[j])
                if j-i+1<k:
                        j+=1
                elif j-i+1==k:
                        if len(neg)==0:
                                res.append(0)
                        else:
                                res.append(neg[0])
                                if arr[i]==neg[0]:
                                        neg.pop(0)
                        i+=1
                        j+=1
        return res

arr = [12, -1, -7, 8, -15, 30, 16, 28]
k = 3
print(firstnegative(arr,k))
