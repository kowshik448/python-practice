class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

class double_llist:
    def __init__(self):
        self.head=None
    
    def append(self,key):
        new_node=Node(key)
        curr=self.head
        if curr is None:
            self.head=new_node
        else:
            while curr.next!=None:
                curr=curr.next
            curr.next=new_node
            # new_node.prev=curr

    
    # def prepend(self,key):
    #     new_node=Node(key)
    #     curr=self.head
    #     if curr is None:
    #         self.head=curr
    #     else:

    def merge_lists(self,left,right):
        if left is None:
            return right
        if right is None:
            return left
        if left.data<=right.data:
            left.next=self.merge_lists(left.next,right)
            left.next.prev=left
            left.prev = None
            return left
        else:
            right.next=self.merge_lists(left,right.next)
            right.next.prev=right
            right.prev=None
            return right

    def merge_sort(self,temphead):
        if temphead is None or temphead.next is None:
            return temphead
        right_head=self.get_middle(temphead)
        left_list=self.merge_sort(temphead)
        right_list=self.merge_sort(right_head)

        return self.merge_lists(left_list,right_list)
    
    
    def get_middle(self,temphead):
        slow=fast=temphead
        while fast.next!=None and fast.next.next!=None:
            slow=slow.next
            fast=fast.next.next
        temp=slow.next
        slow.next=None
        return temp


    # def print_list(self,node):
    #     while node is not None:
    #         print(node.data)
    #         node=node.next
    
    def print_list(self):
        curr=self.head
        while curr!=None:
            print(curr.data)
            curr=curr.next
        

d=double_llist()
d.append(10)
d.append(2)
d.append(32)
d.append(0)
d.append(31)
d.head=d.merge_sort(d.head)
# d.print_list(d.head)