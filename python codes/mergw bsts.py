class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
#merge 2 balanced binary search trees 
def merge_lists(arr1,arr2):# 2 lists are sorted
    arr=[]
    i=j=0
    while i<len(arr1) and j<len(arr2):
        if arr1[i]<arr2[j]:
            arr.append(arr1[i])
            i+=1
        else:
            arr.append(arr2[j])
            j+=1
    while i<len(arr1):
        arr.append(arr1[i])
        i+=1
    while j<len(arr2):
        arr.append(arr2[j])
        j+=1
    return arr

def insert(root,data):
    if not root:
        return Node(data)
    if root.data<data:
        root.right=insert(root.right,data)
    elif root.data>data:
        root.left=insert(root.left,data)
    else:
        return root
    return root

def arr_to_bst(arr):
    l=len(arr)
    if l==0:
        return None
    mid=l//2
    root=Node(arr[mid])
    left=arr[:mid]
    right=arr[mid+1:]
    root.left=arr_to_bst(left)
    root.right=arr_to_bst(right)
    return root


def inorder(root,arr=[]):
    if root:
        inorder(root.left,arr)
        arr.append(root.data)
        inorder(root.right,arr)

root1=None
root2=None

root1=insert(root1,100)
root1=insert(root1,50)
root1=insert(root1,300)
root1=insert(root1,20)
root1=insert(root1,70)

root2=insert(root2,80)
root2=insert(root2,40)
root2=insert(root2,120)

arr1=[]
arr2=[]
inorder(root1,arr1)
print(arr1)
inorder(root2,arr2)
print(arr2)
arr=merge_lists(arr1,arr2)
print(arr)
root=arr_to_bst(arr)
res=[]
inorder(root,res)
print(res)