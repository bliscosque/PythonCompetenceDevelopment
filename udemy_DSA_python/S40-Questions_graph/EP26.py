class Node: 
	def __init__(self, key): 
		self.data = key 
		self.left = None
		self.right = None

def insert(node, data):
   if node is None:
       return Node(data)
   else:
       if data <= node.data:
           temp = insert(node.left, data)
           node.left = temp
           temp.parent = node
       else:
           temp = insert(node.right, data)
           node.right = temp
           temp.parent = node      
       return node

def minVal(node):
    cur=node
    while cur is not None:
        if cur.left is None: break
        cur=cur.left
    return cur

def inOrderSuccessor(root, n):
    if n.right is not None:
        return minVal(n.right)
    p=n.parent
    while p is not None:
        if n!=p.right: break
        n=p
        p=p.parent
    return p

root = None
root = insert(root, 4)
root = insert(root, 2)
root = insert(root, 8)
root = insert(root, 1)
root = insert(root, 3)
root = insert(root, 5)
root = insert(root, 9)

temp = root.left #2

successor = inOrderSuccessor(root, temp)
print(successor.data)

if successor is not None:
    print("Inorder successor of %d is %d" %(temp.data, successor.data))
else:
    print("Inorder successor does not exist")