class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Linked_list():
    def __init__(self):
        self.head = None
    
    def print_list(self):
        if self.head is None:
            print('linked list is empty')
            return
        x = self.head
        while x is not None:
            print(x.data)
            x = x.next

    def print_list(self,node):
        while node!=None:
            print(node.data)
            node=node.next
    
    def length(self):
        x=self.head
        count=0
        while x is not None:
            count+=1
            x=x.next
        return count
    
    def append(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head=new_node
        else:
            x = self.head
            while x.next is not None:
                x=x.next
            x.next=new_node

    def prepend(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head=new_node
        else:
            new_node.next = self.head
            self.head = new_node
    
    def insert_after(self,data,n):
        new_node = Node(data)
        x = self.head
        while x is not None:
            if x.data==n:
                break
            x = x.next
        if x is None:
            print('given node is not in the linked list')
        else:
            new_node.next = x.next
            x.next = new_node
    
    def insert_before(self,data,n):
        new_node = Node(data)
        if self.head is None:
            print('linked list is empty')
            return

        if self.head.data==n:
            new_node.next = self.head
            self.head = new_node
            return
        x = self.head
        while x.next is not None:
            if x.next.data == n:
                break
            x = x.next
        if x.next is None:
            print('node is not found')
        else:
            new_node.next = x.next
            x.next=new_node
    
    def empty_list(self,data):
        if self.head is None:
            new_node = Node(data)
            self.head=new_node
        else:
            print('linked list is not empty')
    
    def swap_node1(self,data1,data2):
    # "this swap node function is not apliclabkle for swapping first node"
        n=self.head
        if data1==data2:
            return
        a = None
        b = None

        while n.next is not None:
            if n.next.data == data1:
                a=n
            elif n.next.data == data2:
                b=n 
            n=n.next
        if a!=None and b!=None :
            temp = a.next
            a.next = b.next
            b.next = temp
            temp1 = a.next.next
            a.next.next = b.next.next
            b.next.next = temp1
        return 
    def swap_node(self,data1,data2):
        if data1 == data2:
            return
        prev1 = None
        curr1 = self.head
        while curr1!=None and curr1.data!=data1:
            prev1=curr1
            curr1=curr1.next
        prev2 = None
        curr2 = self.head
        while curr2!=None and curr2.data!=data2:
            prev2=curr2
            curr2 = curr2.next
        
        if curr1 == None or curr2== None :
            return
        if prev1!=None:
            prev1.next = curr2
        else:
            self.head = curr2
        if prev2!=None:
            prev2.next= curr1
        else:
            self.head = curr1
        
        temp = curr1.next
        curr1.next = curr2.next
        curr2.next = temp

    def reverse_1(self):
        prev = None
        curr = self.head
        while curr is not None:
            temp = curr.next
            curr.next=prev
            prev = curr
            curr = temp
        self.head = prev
    
    def reccursive(self,curr,prev):
        if curr.next is None:
            self.head = curr
            curr.next = prev
            return
        temp = curr.next
        curr.next = prev
        prev  = curr
        curr = temp
        self.reccursive(curr,prev)

    def reverse_2(self):
        if self.head is None:
            return
        self.reccursive(self.head,None)
    
    def delete_node(self,position):
        x = self.head
        n=self.length()
        if position>=n or position<0:
            return
        elif position==0:
            self.head=x.next
        elif 0<position<n:
            for _ in range(position-1):
                x=x.next
            temp=x.next.next
            x.next=temp
    
    def remove_duplicates(self):
        arr=[]
        curr=self.head
        prev=None
        while curr is not None:
            if curr.data in arr:
                prev.next=curr.next
            else:
                arr.append(curr.data)
                prev = curr
            curr=prev.next

    def add_lists(self,list1,list2):
        prev=None
        carry=0
        while (list1 is not None or list2 is not None):
            l1= 0 if list1 is None else list1.data
            l2= 0 if list2 is None else list2.data
            sum = l1+l2+carry
            carry=1 if sum>=10 else 0
            sum= sum if sum<10 else sum%10
            new_node=Node(sum)
            if self.head is None:
                self.head=new_node
            else:
                prev.next=new_node
            prev=new_node
            if list1 is not None:
                list1=list1.next
            if list2 is not None:
                list2=list2.next
        if carry>0:
            new_node=Node(carry)
            prev.next=new_node
    
    def detectAndRemoveloop(self):
        s_ptr=f_ptr=self.head
        while (s_ptr and f_ptr and f_ptr.next):
            s_ptr=s_ptr.next
            f_ptr=f_ptr.next.next
            if s_ptr==f_ptr:
                self.removeloop(s_ptr)
                return True
        return 0
    
    # def removeloop(self,s_ptr):
    #     ptr1=self.head
    #     while True:
    #         ptr2=s_ptr
    #         while ptr2.next!=s_ptr and ptr2.next!=ptr1:
    #             ptr2=ptr2.next
    #         if ptr2.next==ptr1:
    #             break
    #         ptr1=ptr1.next
    #     ptr2.next=None
    
    def removeloop(self,s_ptr):
        ptr1=self.head
        ptr3=self.head
        ptr2=s_ptr
        count=1
        while ptr2.next!=s_ptr:
            count+=1
        k=0
        while k<count:
            ptr3=ptr3.next
            k+=1
        ptr3=self.head
        while ptr3!=ptr1:
            ptr1=ptr1.next
            ptr3=ptr3.next
        while ptr1.next!=ptr3:
            ptr1=ptr1.next
        ptr1.next=None

        
    def rotate(self,k): #k is index
        if k==0:
            return 
        n=1
        curr=self.head
        while curr is not None and n<k:
            curr=curr.next
            n+=1
        if curr is None:
            return 
        knode=curr
        curr = self.head
        while curr.next is not None:
            curr=curr.next
        curr.next=self.head
        self.head=knode.next
        knode.next=None
    
    def merge_sortedlists(self,list1): #3 pointer method inside a class
        p = self.head
        q = list1.head
        s = None
        if p is None:
            return q
        if q is None:
            return p
        if p.data<=q.data:
            s=p
            p=p.next
        else:
            s=q
            q=q.next
        head_ref=s
        while p and q:
            if p.data<=q.data:
                s.next=p
                s=p
                p=p.next
            else:
                s.next=q
                s=q
                q=q.next
        if p is None:
            s.next=q
        if q is None:
            s.next=p
        return head_ref
        
#  'merging through reccursion'
    def merge_lists(self,headA,headB):
        temp=None
        if headA is None:
            return headB
        if headB is None:
            return headA
        if headA.data<=headB.data:
            temp=headA
            temp.next=self.merge_lists(headA.next,headB)
        else:
            temp = headB
            temp.next=self.merge_lists(headA,headB.next)
        return temp

    def merge_sort(self,x):#x is head
        if x is None or x.next is None :
            return x
        middle=self.get_middle(x)
        middle_next=middle.next
        middle.next=None
        left_list=self.merge_sort(x)
        right_list=self.merge_sort(middle_next)
        sorted_list = self.merge_lists(left_list,right_list)
        return sorted_list
    
    def get_middle(self,x):
        slow=fast=x
        while fast.next!=None and fast.next.next!=None:
            slow=slow.next
            fast=fast.next.next
        return slow
    
"merge lists using dummy_node outside the class"    
# def merge_lists(headA,headB):
#     dummy_node=Node(0)
#     tail=dummy_node
#     while True:
#         if headA is None:
#             tail.next=headB
#             break
#         if headB is None:
#             tail.next=headA
#             break
#         if headA.data<=headB.data:
#             tail.next=headA
#             headA=headA.next
#         else:
#             tail.next=headB
#             headB=headB.next
#         tail=tail.next
#     return dummy_node.next




# llist=Linked_list()
# llist.append('2')
# llist.prepend('1')
# llist.insert_after('4','2')
# llist.insert_before('3','4')
# llist.print_list()
# llist.remove_duplicates()
# print('\nnew list')
# llist.delete_node(0)
# llist.swap_node1('b','a')
# llist.reverse_2()
# llist.print_list()
list1=Linked_list()
# list2=Linked_list()
list1.append(1)
list1.append(3)
list1.append(5)
list1.append(7)
list1.append(9)
# llist.head.next.next.next.next.next=llist.head.next.next.next
# llist.detectAndRemoveloop()
# llist.rotate(0)
# llist.print_list()
list1.append(2)
list1.append(4)
list1.append(6)
list1.append(10)
list1.head=list1.merge_sort(list1.head)
# list1.head=list1.merge_sortedlists(list2)
list1.print_list(list1.head)
# res=Linked_list()
# res.add_lists(list1.head,list2.head)
# res.print_list()