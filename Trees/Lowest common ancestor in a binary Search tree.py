#time complexity: O(height of tree)
#space complexity: O(1)
# A recursive python program to find LCA of two nodes
# n1 and n2

# A Binary tree node
class Node:

	# Constructor to create a new node
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

# Function to find LCA of n1 and n2.
# The function assumes that both
# n1 and n2 are present in BST
def lca(root, n1, n2):
	while root:
		# If both n1 and n2 are smaller than root,
		# then LCA lies in left
		if root.data > n1 and root.data > n2:
			root = root.left
		
		# If both n1 and n2 are greater than root,
		# then LCA lies in right
		elif root.data < n1 and root.data < n2:
			root = root.right

		else:
			break

	return root

# Driver program to test above function
# Let us construct the BST shown in the figure
root = Node(20)
root.left = Node(8)
root.right = Node(22)
root.left.left = Node(4)
root.left.right = Node(12)
root.left.right.left = Node(10)
root.left.right.right = Node(14)

n1 = 10 ; n2 = 14
t = lca(root, n1, n2)
print "LCA of %d and %d is %d" %(n1, n2, t.data)

n1 = 14 ; n2 = 8
t = lca(root, n1, n2)
print "LCA of %d and %d is %d" %(n1, n2 , t.data)

n1 = 10 ; n2 = 22
t = lca(root, n1, n2)
print "LCA of %d and %d is %d" %(n1, n2, t.data)

