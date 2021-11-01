class Node:
    def __init__(self,value):
        self.left=None
        self.data=value
        self.right=None
        self.level=None

class Tree:
    def createNode(self,data):
        return Node(data)
    def insert(self,node,data):
        if node is None:
            return self.createNode(data)
        if data<node.data:
            node.left=self.insert(node.left,data)
        else:
            node.right=self.insert(node.right,data)
        return node

    def Inorder(self,root):
        if root is not None:
            self.Inorder(root.left)
            print(root.data,end=" ")
            self.Inorder(root.right)
    '''        
    def Inorder(self,root):
        stack=[]
        result=[]
        while root is not None or stack!=[]:
            while root is not None:
                stack.append(root)
                root=root.left
            root=stack.pop()
            result.append(root.data)
            root=root.right
    '''    
    def preOrder(self,root):
        if root is not None:
            print(root.data,end=' ')
            self.preOrder(root.left)
            self.preOrder(root.right)
            
    def postOrder(self,root):
        if root is not None:
            self.postOrder(root.left)
            self.postOrder(root.right)
            print(root.data,end=' ')
            
    def height(self,root):
        if root is None:
            return -1
        return max(self.height(root.left),self.height(root.right))+1
    
    def levelOrder(self,root):
        q=[]
        q.append(root)
        while len(q)!=0:
            root=q.pop(0)
            print(root.data,end=' ')
            if root.left is not None:
                q.append(root.left)
            if root.right is not None:
                q.append(root.right)
                
    def checkBST(self,root):
        def In_order(root,values):
            if root is None:
                return
            In_order(root.left,values)
            values.append(root.data)
            In_order(root.right,values)
        values=[]
        In_order(root,values)
        for i in range(len(values)-1):
            if values[i]>=values[i+1]:
                return False
        return True
    
    def topView(self,root):
        q=[]
        d=dict()
        root.level=0
        q.append(root)
        while len(q)!=0:
            root=q.pop(0)
            if root.level not in d:
                d[root.level]=root.data
            if root.left is not None:
                q.append(root.left)
                root.left.level=root.level-1
            if root.right is not None:
                q.append(root.right)
                root.right.level=root.level+1
        for i in sorted(d):
            print(d[i],end=' ')
obj=Tree()
root=obj.createNode(5)
obj.insert(root,2)
obj.insert(root ,10)
obj.insert(root ,7)
obj.insert(root ,15)
obj.insert(root ,12)
obj.insert(root ,20)
obj.insert(root ,30)
obj.insert(root ,6)
obj.insert(root ,8)
print("------Inorder traversal------")
obj.Inorder(root)
print()
print("------Preorder traversal------")
obj.preOrder(root)
print()
print("------Postorder traversal------")
obj.postOrder(root)
print()
print("------Height------")
print(obj.height(root))
print("------levelorder traversal------")
obj.levelOrder(root)
print()
print("----checkBst------")
print(obj.checkBST(root))
print("------Top View L->R ------")
obj.topView(root)
