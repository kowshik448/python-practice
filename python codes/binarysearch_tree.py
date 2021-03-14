class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class Binary_search_tree:
    def __init__(self,data):
        self.root=Node(data)
    
    def insert(self,curr_node,data):
        if curr_node is None:
            return Node(data)
        else:
            if curr_node.data==data:
                return curr_node
            elif data>curr_node.data:
                curr_node.right=self.insert(curr_node.right,data)
            elif data<curr_node.data:
                curr_node.left=self.insert(curr_node.left,data)
        return curr_node
    
    def search(self,curr_node,data):
        if curr_node:
            if curr_node.data==data:
                return True
            elif curr_node.data<data:
                return self.search(curr_node.right,data)
            else:
                return self.search(curr_node.left,data)
        return False
    
    def min_element(self,root):
        if root is None:
            return None
        while root.left!=None:
            root=root.left
        return root
    
    def delete(self,root,data):
        if root is None:
            return None
        if root.data<data:
            root.right=self.delete(root.right,data)
        elif root.data>data:
            root.left=self.delete(root.left,data)
        else:
            if not root.left:
                temp=root.right
                root=None
                return temp
            elif not root.right:
                temp=root.left
                root=None
                return temp
            else:
                temp=self.min_element(root.right)#inorder successor
                root.data=temp.data
                root.right=self.delete(root.right,temp.data)
        return root

    def lca(self,root,n1,n2):#least common ancestor
        if root is None:
            return None
        if root.data<n1 and root.data<n2:
            return self.lca(root.right,n1,n2)
        elif root.data>n1 and root.data>n2:
            return self.lca(root.left,n1,n2)
        else:
            return root.data
    
    def findpresuc(self,root,findpresuc_pre,findpresuc_suc,data):
        if root is None:
            return 
        if root.data==data:
            if root.left :
                temp=root.left
                while temp.right:
                    temp=temp.right
                findpresuc_pre=temp
            if root.right:
                temp=root.right
                while temp.left:
                    temp=temp.left
                findpresuc_suc=temp
            return 
        if root.data>data:
            findpresuc_suc=root
            self.findpresuc(root.left,findpresuc_pre,findpresuc_suc,data)
        else:
            findpresuc_pre=root
            self.findpresuc(root.right,findpresuc_pre,findpresuc_suc,data)
            
    def inorder_succ(self,root,curr):
        if curr.right :
            return self.min_element(curr.right)
        succ=Node(None)
        while root:
            if root.data>curr.data:
                succ=root
                root=root.left
            elif root.data<curr.data:
                root=root.right
            else:
                return succ

    # def kth_smallest(self,node):
    #     if node is None:
    #         return None
    #     global k
    #     left=self.kth_smallest(node.left)
    #     if left:
    #         return left
    #     # k-=1
    #     if k==0:
    #         return node
    #     right=self.kth_smallest(node.right)
    #     return right
    
    def correctBSTutil(self,root,first,middle,last,prev):
        if root:
            self.correctBSTutil(root.left,first,middle,last,prev)
            if prev[0] and prev[0].data>root.data:
                if first[0]:
                    last[0]=root
                else:
                    first[0]=prev[0]
                    middle[0]=root
            prev[0]=root
            self.correctBSTutil(root.right,first,middle,last,prev)

    
    def correct_bst(self,root):
        if root is None:
            return 
        first=[None]
        middle=[None]
        last=[None]
        prev=[None]
        self.correctBSTutil(root,first,middle,last,prev)
        if first[0] and last[0]:
            first[0].data,last[0].data=last[0].data,first[0].data
        elif first[0] and middle[0]:
            first[0].data,middle[0].data=middle[0].data,first[0].data
    
    def floor_ceil(self,root,n):#iterative approach
        global floor,ceil
        while root:
            if root.data==n:
                floor=root.data
                ceil=root.data
                break
            elif root.data<n:
                floor=root.data
                root=root.right
            else:
                ceil=root.data
                root=root.left
    
    def change_values(self,root,arr):
        if root:
            self.change_values(root.left,arr)
            root.data=arr[0]
            arr.pop(0)
            self.change_values(root.right,arr)
    
    def in_arr(self,root,arr):
        if root:
            self.in_arr(root.left,arr)
            arr.append(root.data)
            self.in_arr(root.right,arr)

    
    def btree_bst(self,root):
        if root is None:
            return None
        arr=[]
        self.in_arr(root,arr)
        arr.sort()
        self.change_values(root,arr)



    
    def inorder(self,node):
        if node:
            self.inorder(node.left)
            print(node.data,end=" ")
            self.inorder(node.right)


# BST=Binary_search_tree(10)
# BST.insert(BST.root,5)
# BST.insert(BST.root,9)
# BST.insert(BST.root,8)
# BST.insert(BST.root,11)
# BST.insert(BST.root,12)
# BST.insert(BST.root,1)
root = Binary_search_tree(6) 
root.root.left = Node(10)  
root.root.right = Node(2)  
root.root.left.left = Node(1)  
root.root.left.right = Node(3)  
root.root.right.left = Node(7)  
root.root.right.right = Node(12)
# print(BST.search(BST.root,6))
# print(BST.lca(BST.root,8,2))
# BST.inorder(BST.root)
# BST.delete(BST.root,8)
# print("\n")
# root.inorder(root.root)
# root.correct_bst(root.root)
# print()
# root.inorder(root.root)
# findpresuc_pre=None
# findpresuc_suc=None
# BST.findpresuc(BST.root,findpresuc_pre,findpresuc_suc,9)
# # if findpresuc_pre:
#     print(findpresuc_pre.data,end=' ')
# else:
#     print(None)
# if findpresuc_suc:
#     print(findpresuc_suc.data,end=" ")
# else:
#     print(None)
# print(findpresuc_pre.data,findpresuc_suc.data)
# print('\n', BST.inorder_succ(BST.root,BST.root).data)
# k=8
# print('\n',(BST.kth_smallest(BST.root)).data)
# floor=-1
# ceil=-1
# BST.floor_ceil(BST.root,9.5)
# print("\n",floor,ceil)
root.inorder(root.root)
root.btree_bst(root.root)
print()
root.inorder(root.root)