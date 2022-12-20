class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left

def findNodeInTree(target,rootNode):
    if not rootNode: return False
    if target==rootNode: return True
    return findNodeInTree(target,rootNode.left) or findNodeInTree(target,rootNode.right)

def findFirstCommonAncestor(n1, n2, root):
    n1Left=findNodeInTree(n1,root.left)
    n2Left=findNodeInTree(n2,root.left)
    if n1Left ^ n2Left: return root #xor
    if n1Left: return findFirstCommonAncestor(n1,n2,root.left)
    else: return findFirstCommonAncestor(n1,n2,root.right)
