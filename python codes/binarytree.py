class Queue():
    def __init__(self):
        self.items=[]
    
    def enqueue(self,key):
        self.items.insert(0,key)
    
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1].data
    
    def is_empty(self):
        return len(self.items)==0
    
    def __len__(self):
        return len(self.items)
    

class Node():
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data

class Binary_tree():
    def __init__(self,data):
        self.root=Node(data)
    
    def print_tree(self,traversal_type):
        if traversal_type=="preorder":
            return self.pre_order_traversal(self.root,[])
        elif traversal_type=="inorder":
            return self.in_order_traversal(self.root)
        elif traversal_type=="postorder":
            return self.post_order_traversal(self.root,"")
        elif traversal_type=="levelorder":
            return self.level_order_traversal(self.root)
        elif traversal_type=="reverselevelorder":
            return self.reverse_levelorder(self.root)
        else:
            print("traversaltype is not supported")
        


    def pre_order_traversal(self,curr,output):
        "root->left->right"
        if curr is not None:
            output.append(curr.data)
            # output+=(str(curr.data)+"-")
            output=self.pre_order_traversal(curr.left,output)
            output=self.pre_order_traversal(curr.right,output)
        return output
    
    # def in_order_traversal(self,curr,output):
    #     "left->root->right"
    #     if curr is not None:
    #         output=self.in_order_traversal(curr.left,output)
    #         output+=(str(curr.data)+"-")
    #         output=self.in_order_traversal(curr.right,output)
    #     return output
    'inorder traveersal without reccursion using stack'
    def in_order_traversal(self,curr):
        stack=[]
        if curr is None:
            return
        while True:
            if curr is not None:
                stack.append(curr)
                curr=curr.left
            elif stack:
                curr=stack.pop()
                print(curr.data,end=" ")
                curr=curr.right
            else:
                break
        

        
    def post_order_traversal(self,curr,output):
        "left->right->root"
        if curr:
            output=self.post_order_traversal(curr.left,output)
            output=self.post_order_traversal(curr.right,output)
            output+=(str(curr.data)+"-")
        return output
    
    def level_order_traversal(self,curr):
        if curr is None:
            return 
        queue=Queue()
        queue.enqueue(curr)
        output=''
        while len(queue)>0:
            output+=str(queue.peek())+"-"
            node=queue.dequeue()
            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)
        return output

    def reverse_levelorder(self,curr):
        if curr is None:
            return 
        queue=Queue()
        queue.enqueue(curr)
        output=''
        while len(queue)>0:
            node=queue.dequeue()
            output=str(node.data)+'-'+output
            if node.right:
                queue.enqueue(node.right)
            if node.left:
                queue.enqueue(node.left)
        return output
    
    def height(self,node):
        if node is None:
            return 0
        left_height=self.height(node.left)
        right_height=self.height(node.right)
        return 1+max(left_height,right_height)
    
    # def size(self):
    #     if self.root is None:
    #         return 0
    #     q=Queue()
    #     q.enqueue(self.root)
    #     count=1
    #     while q:
    #         node=q.dequeue()
    #         if node.left:
    #             count+=1
    #             q.enqueue(node.left)
    #         if node.right:
    #             count+=1
    #             q.enqueue(node.right)
    #     return count
    
    def size(self,node):# size is number of nodes 
        if node is None:
            return 0
        return 1+self.size(node.left)+self.size(node.right)

    def diameter(self,node):
        if node is None:
            return 0
        l_height=self.height(node.left)
        r_height=self.height(node.right)

        l_diameter=self.diameter(node.left)
        r_diameter=self.diameter(node.right)
        
        return max(l_height+r_height+1,max(l_diameter,r_diameter))
    

    def max_width(self,node):#O(N2)
        max_width=0
        h=self.height(node)
        for i in range(1,h+1):
            width=self.get_width(node,i)
            if width>max_width:
                max_width=width
        return max_width
    

    def get_width(self,root,level):
        if root is None:
            return 0
        if level==1:
            return 1
        elif level>1:
            return self.get_width(root.left,level-1)+self.get_width(root.right,level-1)

    def get_max_width(self,node):
        if node is None:
            return 0
        max_width=0
        q=Queue()
        q.enqueue(node)
        while not q.is_empty():
            count=len(q)
            max_width=max(count,max_width)
            while count!=0:
                temp=q.dequeue()
                if temp.left:
                    q.enqueue(temp.left)
                if temp.right:
                    q.enqueue(temp.right)
                count-=1
        return max_width

    
    def getmaxwidth(self,node):
        if node is None:
            return 0
        h=self.height(node)
        count_array=[0]*h
        level=0
        self.maxwidth_reccur(node,count_array,level)
        return max(count_array)


    def maxwidth_reccur(self,node,count_array,level):
        if node:
            count_array[level]+=1
            self.maxwidth_reccur(node.left,count_array,level+1)
            self.maxwidth_reccur(node.right,count_array,level+1)
    
    "printing nodes at k distance from the root"
    def k_distance(self,node,k):
        if node is None:
            return 
        if k==0:
            print(node.data,end=" ")
        if k>=1:
            self.k_distance(node.left,k-1)
            self.k_distance(node.right,k-1)
    
    "ancestors of k"
    def print_ancestors(self,node,k):
        if node is None:
            return False
        if node.data==k:
            return True
        if self.print_ancestors(node.left,k) or self.print_ancestors(node.right,k):
            print(node.data,end=" ")
            return True
        return False


    
    def build_tree(self,inorder,preorder):
        if not inorder or not preorder:
            return None
        root=Node(preorder[0])
        index=inorder.index(preorder[0])
        root.left=self.build_tree(inorder[:index],preorder[1:index+1])
        root.right=self.build_tree(inorder[index+1:],preorder[index+1:])
        return root
    






tree=Binary_tree(1)
tree.root.left=Node(2)
tree.root.right=Node(3)
tree.root.left.left=Node(4)
tree.root.left.right=Node(5)
tree.root.right.left=Node(6)
tree.root.right.right=Node(7)
tree.root.right.left.right=Node(8)
print(tree.print_tree("preorder"))
# tree.print_tree("inorder")
# print(tree.print_tree("postorder"))
# print(tree.print_tree("reverselevelorder"))
# print(tree.size(tree.root))
# print(tree.diameter(tree.root))
# inorder=[4,2,5,1,6,3,7]
# preorder=[1,2,4,5,3,6,7]
# tree.root=tree.build_tree(inorder,preorder)
# print(tree.root)
# print(tree.getmaxwidth(tree.root))
# tree.k_distance(tree.root,2)
# tree.print_ancestors(tree.root,8)