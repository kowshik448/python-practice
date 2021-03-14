class Node:
    def __init__(self,data):
        self.next=None
        self.data=data

class Linked_list():
    def __init__(self):
        self.head=None
    
    def Print_list(self):
        if self.head is None:
            return None
        x= self.head
        while x:
            print(x.data)
            x=x.next
    
    def lenght(self):
        x =self.head
        count=0
        while x:
            count+=1
            x=x.next
        return count
    
    def append(self,data):
        if self.head is None:
            return self.head=Node(data)
        x=self.head
        while x.next:
            x=x.next
        x.next=Node(data)
    
    def prepend(self,data):
        if self.head is None:
            return self.head=Node(data)
        x=self.head
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node
    
    def insert_after(self,key,data):
        x=self.head
        new_node=Node(data)
        while x:
            if x.data==key:
                new_node.next=x.next
                x.next=new_node
                break
            x=x.next
        if x is None:
            return None
    
    def insert_before(self,key,data):
