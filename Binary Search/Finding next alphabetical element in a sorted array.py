
def alphabeticalSearch(arr, low, high, x): 

	# If x is smaller than or equal to the first element, 
	# then return the first element */ 
	if x <= arr[low]: 
		return arr[low] 

	# If x is greater than the last element, then return -1 */ 
	if x > arr[high]: 
		return '#'

	# get the index of middle element of arr[low..high]*/ 
	mid =  low + (high - low)//2 

	# If x is same as middle element, then return mid */ 
	if arr[mid] == x: 
		return alphabeticalSearch(arr, mid+1, high, x) 

	# If x is greater than arr[mid], then either arr[mid + 1] 
	# is ceiling of x or ceiling lies in arr[mid+1...high] */ 
	elif arr[mid] < x: 
		if mid + 1 <= high and x <= arr[mid+1]: 
			return arr[mid + 1]
		else: 
			return alphabeticalSearch(arr, mid+1, high, x) 

	# If x is smaller than arr[mid], then either arr[mid] 
	# is ceiling of x or ceiling lies in arr[low...mid-1] */ 
	else: 
		if mid - 1 >= low and x > arr[mid-1]: 
			return arr[mid] 
		else: 
			return alphabeticalSearch(arr, low, mid - 1, x) 

# Driver program to check above functions */ 
arr = ['a', 'd', 'e', 'f', 'g', 'j', 'k'] 
n = len(arr) 
x = 'i'
index = alphabeticalSearch(arr, 0, n-1, x); 

if index == '#': 
	print ("Ceiling of %c doesn't exist in array "% x) 
else: 
	print ("ceiling of %c is %c"%(x, index)) 

 
