class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Circular_linkedlist():
    def __init__(self):
        self.head=None

    def append(self,data):
        new_node=Node(data)
        curr=self.head
        if curr is None:
            self.head=new_node
            new_node.next=self.head
        else:
            while curr.next!=self.head:
                curr=curr.next
            curr.next=new_node
            new_node.next=self.head
    
    def prepend(self,data):
        new_node=Node(data)
        curr=self.head
        if curr is None:
            self.head=new_node
            new_node.next=self.head
        else:
            while curr.next!=self.head:
                curr=curr.next
            curr.next=new_node
            new_node.next=self.head
            self.head=new_node
    
    def insert_after(self,data,data1):#have to add after data1
        new_node=Node(data)
        curr=self.head
        if self.head is None:
            return
        if self.head.data==data1:
            temp=self.head.next
            self.head.next=new_node
            new_node.next=temp
        curr=curr.next
        while curr!=self.head:
            if curr.data==data1:
                temp=curr.next
                curr.next=new_node
                new_node.next=temp
            curr=curr.next
    
    def __len__(self):
        curr=self.head
        count=0
        while curr:
            count+=1
            curr=curr.next
            if curr==self.head:
                break
        return count
    
    def split_list(self):
        curr=self.head
        if curr is None:
            return 
        if curr.next==self.head:
            return 
        else:
            mid=len(clist)//2
            count=0
            prev=None
            while count<mid:
                prev=curr
                curr=curr.next
                count+=1
            prev.next=self.head
            clist2=Circular_linkedlist()
            while curr!=self.head:
                clist2.append(curr.data)
                curr=curr.next
            self.print_list()
            print("\n")
            clist2.print_list()
    
    def sorted_insert(self,new_node):
        curr=self.head
        if curr is None:
            new_node.next=self.head
            self.head=new_node
        elif curr.data>=new_node:
            # alternate method(efficient method)
            # curr.data , new_node.data=new_node.data , curr.data
            # new_node.next=curr.next
            # curr.next=new_node
            while curr.next!=self.head:
                curr=curr.next
            curr.next=new_node
            new_node.next=self.head
            self.head=new_node
        else:
            while curr.next!=self.head and curr.next.data<=new_node.data:
                curr=curr.next
            new_node.next=curr.next
            curr.next=new_node


    def remove(self,key):
        curr=self.head
        if curr is None:
            return 
        if self.head.data==key:
            x = self.head
            while x.next!=self.head:
                x=x.next
            x.next=self.head.next
            self.head=self.head.next
        prev=None
        while curr.next!=self.head:
            prev=curr
            curr=curr.next
            if curr.data==key:
                prev.next=curr.next
        
    def print_list(self):
        curr=self.head
        if curr is None:
            return
        print(curr.data)
        curr=curr.next
        while curr!=self.head:
            print(curr.data)
            curr=curr.next
        

        
    
clist=Circular_linkedlist()
clist.prepend(1)
clist.prepend(2)
clist.prepend(3)
clist.prepend(4)
clist.append(0)
clist.print_list()
print("new list")
clist.remove(56)
# clist.insert_after(0,1)
clist.print_list()