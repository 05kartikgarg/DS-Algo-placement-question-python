class Node:
    def __init__(self,value):
        self.data=value
        self.next=None
        
class LinkedList:
    def __init__(self):
        self.head=None
        
    def insert(self,value):
        new_node=Node(value)
        new_node.next=self.head
        self.head=new_node

    def reverse(self):
        current=self.head
        prev=None
        while current is not None:
            nex=current.next
            current.next=prev
            prev=current
            current=nex
        self.head=prev
        
    def traverse(self):
        temp=self.head
        while temp is not None:
            print(temp.data,end=" ")
            temp=temp.next
        print()
obj=LinkedList()
obj.insert(5)
obj.insert(10)
obj.insert(15)
obj.insert(20)
obj.insert(25)
obj.traverse()
obj.reverse()
obj.traverse()
