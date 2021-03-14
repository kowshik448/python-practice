class Node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data

class Binary_tree():
    def __init__(self,data):
        self.root=Node(data)
    
    def morris_tree(self,curr):
        while curr is not None:
            if not curr.left:
                print(curr.data,end=" ")
                curr=curr.right
            else:
                predecessor=curr.left
                while predecessor.right!=None and predecessor.right!=curr:
                    predecessor=predecessor.right
                if predecessor.right==None:
                    predecessor.right=curr
                    curr=curr.left
                else:
                    predecessor.right=None
                    print(curr.data,end=" ")
                    curr=curr.right

tree=Binary_tree(1)
tree.root.left=Node(2)
tree.root.right=Node(3)
tree.root.left.left=Node(4)
tree.root.left.right=Node(5)
tree.root.right.left=Node(6)
tree.root.right.right=Node(7)
tree.root.right.left.right=Node(8)
tree.morris_tree(tree.root)

                
                
