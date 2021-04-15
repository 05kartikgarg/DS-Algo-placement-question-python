'''
#creation of a node

class Node:
    def __init__(self,value):
        self.data=value
        self.next=None
a=Node(5)
b=Node(10)
a.next=b
print(a.data)
'''

#Single linked List Implementation
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
        
    def insert_at_pos(self,pos,value):
        temp=self.head
        while temp is not None:
            if temp.data==pos:
                break
            else:
                temp=temp.next
        if temp is None:
            print("Node not found")
        else:
            new_node=Node(value)
            new_node.next=temp.next
            temp.next=new_node
            print("Node inserted successfully")

    def insert_at_end(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
        else:
            temp=self.head
            while temp.next is not None:
                temp=temp.next
            temp.next=new_node

    def delete_at_beg(self):
        if self.head is None:
            print("Linked List is empty")
        else:
            temp=self.head
            self.head=self.head.next
            del temp
            
    def delete_at_pos(self,value):
        temp=self.head
        while temp.next is not None:
            if temp.next.data==value:
                break
            temp=temp.next
        temp.next=temp.next.next

        
    def delete_at_end(self):
        if self.head is None:
            print("Linked List is empty")
        else:
            temp=self.head
            while temp.next.next is not None:
                temp=temp.next
            temp.next=None
            print("Node deleted successfully!!")
            
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
obj.traverse()
obj.insert_at_pos(10,13)
obj.insert_at_end(2)
obj.traverse()
obj.delete_at_beg()
obj.traverse()
obj.delete_at_end()
obj.traverse()
obj.delete_at_pos(13)
obj.traverse()





        
