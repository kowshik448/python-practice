class Node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.nextright=None
        self.data=data
def connect_nodes(node):
    if node is None:
        return
    q=[]
    q.append(node)
    q.append(None)
    while q:
        p=q.pop(0)
        if p:
            p.nextright=q[0]
            if p.left:
                q.append(p.left)
            if p.right:
                q.append(p.right)
        elif q:
            q.append(None)