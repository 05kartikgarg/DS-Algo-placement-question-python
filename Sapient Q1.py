def min(a, n):
	minIndex = 0
	minValue = a[0]
	
	for i in range(1, n):
		if (a[i] < minValue):
			minValue = a[i]
			minIndex = i
	return minIndex

def maximizeMin(A, N, S, M):
	
	minIndex, left, right = 0, 0, 0
	
	for i in range(M):
		minIndex = min(A, N)

		A[minIndex] += 1

		left = minIndex - 1
		right = minIndex + 1

		for j in range(S - 1):
			
			if (left == -1):
				A[right] += 1
				right += 1
				
			elif (right == N):
				A[left] += 1
				left -= 1

			else:

				if (A[left] < A[right]):
					A[left] += 1
					left -= 1
				
				else:
					A[right] += 1
					right += 1

	minIndex = min(A, N)
	return A[minIndex]


	
arr = [10,2,7]
N = len(arr)
S = 3
M = 3
print(maximizeMin(arr, N, S, M))


