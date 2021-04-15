class Node:
    def __init__(self,data):
        self.next=None
        self.prev=None
        self.data=data

class DoubleLinkedList:
    def __init__(self):
        self.head=None
        
    def insert_beg(self,value):
        new_node=Node(value)
        new_node.prev=None
        new_node.next=self.head
        self.head=new_node
        print("Data Inserted at beggining")

    def insertAfter(self, prev_node, new_data):
        new_node=Node(new_data)
        if self.head is None:
            print("Node not found Linked List is empty")
        else:
            temp=self.head
            while temp.next is not None:
                if temp.data==prev_node:
                    break
                temp=temp.next
            new_node.next=temp.next
            new_node.prev=temp
            temp.next=new_node
            if new_node.next is not None:
                new_node.next.prev=new_node

    def insert_at_end(self,new_data):
        new_node=Node(new_data)
        temp=self.head
        while temp.next is not None:
            temp=temp.next
        temp.next=new_node
        new_node.prev=temp
        new_node.next=None
        
    def delete_head(self):
        if self.head is None:
            print("Cannot delete list already empty")
        else:
            self.head=self.head.next
            self.head.prev=None
            print("Deletion Successfull")
            
    def delete_particular_node(self,node_data):
        temp=self.head
        while temp.next is not None:
            if temp.data==node_data:
                break
            temp=temp.next
        temp.next.prev=temp.prev
        temp.prev.next=temp.next
        temp.next=None
        temp.prev=None    

    def delete_end(self):
        if self.head is None:
            print("Cannot delete list already empty")
        else:
            temp=self.head
            while temp.next.next is not None:
                temp=temp.next
            temp.next.prev=None
            temp.next=None
   
    def traverse(self):
        temp=self.head
        while temp is not None:
            print(temp.data,end=" ")
            temp=temp.next
        print()
        
obj=DoubleLinkedList()
obj.insert_beg(5)
obj.insert_beg(10)
obj.insert_beg(15)
obj.traverse()
obj.insertAfter(10,12)
obj.traverse()
obj.insert_at_end(20)
obj.traverse()
obj.delete_head()
obj.traverse()
obj.delete_end()
obj.traverse()
obj.delete_particular_node(12)
obj.traverse()
