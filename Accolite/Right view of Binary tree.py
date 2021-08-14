# Python3 program to print right view of
# Binary Tree

# Binary Tree Node
""" utility that allocates a newNode
with the given key """
class newNode:

	# Construct to create a newNode
	def __init__(self, key):
		self.data = key
		self.left = None
		self.right = None
		self.hd = 0

# function to print right view of
# binary tree
def printRightView(root):

	if (not root):
		return

	q = []
	q.append(root)

	while (len(q)):
		
		# number of nodes at current level
		n = len(q)
		
		# Traverse all nodes of current level
		for i in range(1, n + 1):		
			temp = q[0]
			q.pop(0)
				
			# Print the right most element
			# at the level
			if (i == n) :
				print(temp.data, end = " " )
			
			# Add left node to queue
			if (temp.left != None) :
				q.append(temp.left)

			# Add right node to queue
			if (temp.right != None) :
				q.append(temp.right)

# Driver Code
if __name__ == '__main__':

	root = newNode(10)
	root.left = newNode(2)
	root.right = newNode(3)
	root.left.left = newNode(7)
	root.left.right = newNode(8)
	root.right.right = newNode(15)
	root.right.left = newNode(12)
	root.right.right.left = newNode(14)
	printRightView(root)


'''
def rightview(self,root):
        result=[]
        level=[]
        queue=[root]
        while queue!=[] and root is not None:
                for node in queue:
                        if node.left:
                                level.append(node.left)
                        if node.right:
                                level.append(node.right)
                result.append(node.val)
                queue=level
                level=[]
        return result


'''








