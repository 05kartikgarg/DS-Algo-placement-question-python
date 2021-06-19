# Simple Python code for check a matrix is
# symmetric or not.

# Fills transpose of mat[N][N] in tr[N][N]
def transpose(mat, tr, N):
	for i in range(N):
		for j in range(N):
			tr[i][j] = mat[j][i]

# Returns true if mat[N][N] is symmetric, else false
def isSymmetric(mat, N):
	
	tr = [ [0 for j in range(len(mat[0])) ] for i in range(len(mat)) ]
	transpose(mat, tr, N)
	for i in range(N):
		for j in range(N):
			if (mat[i][j] != tr[i][j]):
				return False
	return True

# Driver code
mat = [ [ 1, 3, 5 ], [ 3, 2, 4 ], [ 5, 4, 1 ] ]
if (isSymmetric(mat, 3)):
	print "Yes"
else:
	print "No"

# This code is contributed by Sachin Bisht
