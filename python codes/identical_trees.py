class Node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data

def are_identical(node1,node2):
    if node1 is None and node2 is None:
        return True
    if node1 is None or node2 is None:
        return False 
    if node1.data==node2.data and are_identical(node1.left,node2.left) and are_identical(node1.right,node2.right):
        return True
    return False

def  is_subtree(S,T):
    if S is None:
        return True
    if T is None:
        return False
    if are_identical(S,T):
        return True
    return is_subtree(S,T.left) or is_subtree(S,T.right)

def inorder_trsversal(node,arr):
    if node is not None:
        arr=inorder_trsversal(node.left,arr)
        arr.append(node.data)
        arr=inorder_trsversal(node.right,arr)
    arr.append('$')
    return arr
    
def preorder_traversal(node,arr):
    if node is not None:
        arr.append(node.data)
        arr=preorder_traversal(node.left,arr)
        arr=preorder_traversal(node.right,arr)
    arr.append("$")
    return arr

def check1(a,b):
    for i in range(tin-sin+1):
        if a[i:i+sin]==b:
            return True
    return False



S=Node(10)
S.left=Node(20)
S.right=Node(30)
S.left.left=Node(40)

T=Node(1)
T.left=Node(10)
T.right=Node(5)
T.left.left=Node(20)
T.left.right=Node(30)
T.left.left.left=Node(40)
# T.left.left.left.left=Node(50)

# if is_subtree(S,T):
#     print("S is a subtree of T")
# else:
#     print("S is not a subtree of T")
T_in=inorder_trsversal(T,[])
S_in=inorder_trsversal(S,[])
T_pre=preorder_traversal(T,[])
S_pre=preorder_traversal(S,[])
tin=len(T_in)
sin=len(S_in)
if check1(T_in,S_in) and check1(T_pre,S_pre):
    print("S is a subtree of  T")
else:
    print("S is not a subtree of T")