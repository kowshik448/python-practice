class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class BST:
    def __init__(self,data):
        self.root=Node(data)
    
    def insert(self,root,data):
        if root is None:
            return Node(data)
        elif root.data==data:
            return root
        elif root.data<data:
            root.right=self.insert(root.right,data)
        elif root.data>data:
            root.left=self.insert(root.left,data)
        return root

    def inorder(self,root,arr):
        if root:
            self.inorder(root.left,arr)
            arr.append(root.data)
            self.inorder(root.right,arr)
    
    def find_pair(self,arr,summ):
        i=0
        j=len(arr)-1
        while i<j:
            if arr[i]+arr[j]==summ:
                return (arr[i],arr[j])
            elif arr[i]+arr[j]>summ:
                j-=1
            else:
                i+=1
        return "NO PAIRS"

bst=BST(15)
# bst.insert(bst.root,15)
bst.insert(bst.root,10)
bst.insert(bst.root,20)
bst.insert(bst.root,8)
bst.insert(bst.root,12)
bst.insert(bst.root,16)
bst.insert(bst.root,25)
print(bst.root.left.data)
arr=[]
bst.inorder(bst.root,arr)
print(arr)
print(bst.find_pair(arr,46))