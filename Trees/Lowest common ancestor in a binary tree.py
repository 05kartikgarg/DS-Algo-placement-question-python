#Method 1
#time complexity: O(n)
#space complexity: O(n)

class Node:
	# Constructor to create a new binary node
	def __init__(self, key):
		self.key = key
		self.left = None
		self.right = None

# Finds the path from root node to given root of the tree.
# Stores the path in a list path[], returns true if path
# exists otherwise false
def findPath( root, path, k):

	# Baes Case
	if root is None:
		return False

	# Store this node is path vector. The node will be
	# removed if not in path from root to k
	path.append(root.key)

	# See if the k is same as root's key
	if root.key == k :
		return True

	# Check if k is found in left or right sub-tree
	if ((root.left != None and findPath(root.left, path, k)) or
			(root.right!= None and findPath(root.right, path, k))):
		return True

	# If not present in subtree rooted with root, remove
	# root from path and return False
	
	path.pop()
	return False

# Returns LCA if node n1 , n2 are present in the given
# binary tre otherwise return -1
def findLCA(root, n1, n2):

	# To store paths to n1 and n2 fromthe root
	path1 = []
	path2 = []

	# Find paths from root to n1 and root to n2.
	# If either n1 or n2 is not present , return -1
	if (not findPath(root, path1, n1) or not findPath(root, path2, n2)):
		return -1

	# Compare the paths to get the first different value
	i = 0
	while(i < len(path1) and i < len(path2)):
		if path1[i] != path2[i]:
			break
		i += 1
	return path1[i-1]


# Driver program to test above function
# Let's create the Binary Tree shown in above diagram
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print "LCA(4, 5) = %d" %(findLCA(root, 4, 5,))
print "LCA(4, 6) = %d" %(findLCA(root, 4, 6))
print "LCA(3, 4) = %d" %(findLCA(root,3,4))
print "LCA(2, 4) = %d" %(findLCA(root,2, 4))

#Method 2
# time complexity: O(n)
#space complexity: O(1)

""" Program to find LCA of n1 and n2 using one traversal of
Binary tree
It handles all cases even when n1 or n2 is not there in tree
"""

# A binary tree node
class Node:

	# Constructor to create a new node
	def __init__(self, key):
		self.key = key
		self.left = None
		self.right = None

# This function retturn pointer to LCA of two given values
# n1 and n2
# v1 is set as true by this function if n1 is found
# v2 is set as true by this function if n2 is found
def findLCAUtil(root, n1, n2, v):
	
	# Base Case
	if root is None:
		return None

	# IF either n1 or n2 matches ith root's key, report
	# the presence by setting v1 or v2 as true and return
	# root (Note that if a key is ancestor of other, then
	# the ancestor key becomes LCA)
	if root.key == n1 :
		v[0] = True
		return root

	if root.key == n2:
		v[1] = True
		return root

	# Look for keys in left and right subtree
	left_lca = findLCAUtil(root.left, n1, n2, v)
	right_lca = findLCAUtil(root.right, n1, n2, v)

	# If both of the above calls return Non-NULL, then one key
	# is present in once subtree and other is present in other,
	# So this node is the LCA
	if left_lca and right_lca:
		return root

	# Otherwise check if left subtree or right subtree is LCA
	return left_lca if left_lca is not None else right_lca


def find(root, k):
	
	# Base Case
	if root is None:
		return False
	
	# If key is present at root, or if left subtree or right
	# subtree , return true
	if (root.key == k or find(root.left, k) or
		find(root.right, k)):
		return True
	
	# Else return false
	return False

# This function returns LCA of n1 and n2 onlue if both
# n1 and n2 are present in tree, otherwise returns None
def findLCA(root, n1, n2):
	
	# Initialize n1 and n2 as not visited
	v = [False, False]

	# Find lac of n1 and n2 using the technique discussed above
	lca = findLCAUtil(root, n1, n2, v)

	# Returns LCA only if both n1 and n2 are present in tree
	if (v[0] and v[1] or v[0] and find(lca, n2) or v[1] and
		find(lca, n1)):
		return lca

	# Else return None
	return None

# Driver program to test above function
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

lca = findLCA(root, 4, 5)

if lca is not None:
	print "LCA(4, 5) = ", lca.key
else :
	print "Keys are not present"

lca = findLCA(root, 4, 10)
if lca is not None:
	print "LCA(4,10) = ", lca.key
else:
	print "Keys are not present"


