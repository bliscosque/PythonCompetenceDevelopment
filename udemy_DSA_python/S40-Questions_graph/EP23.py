#   Created by Elshad Karimov 
#   Copyright © AppMillers. All rights reserved.

# List of Depth
class LinkedList:
    def __init__(self, val):
        self.val = val
        self.next = None
    
    def add(self, val):
        if self.next == None:
            self.next = LinkedList(val)
        else:
            self.next.add(val)
    def __str__(self):
        return "({val})".format(val = self.val) + str(self.next)

class BinaryTree:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    
def depth(tree):
    if tree==None: return 0
    if tree.left==None and tree.right==None: return 1
    depthL=1+depth(tree.left) #left
    depthR=1+depth(tree.right) #right
    return max(depthL,depthR)

#usando pre-order traversal
#d=depth
def treeToLinkedList(tree, custDict = {}, d = None):
    if d==None: d=depth(tree)
    if custDict.get(d)==None: custDict[d]=LinkedList(tree.val)
    else:
        custDict[d].add(tree.val)
        if d==1: return custDict
    if tree.left!=None:
        custDict=treeToLinkedList(tree.left,custDict,d-1)
    if tree.right!=None:
        custDict=treeToLinkedList(tree.right,custDict,d-1)
    return custDict

mainTree = BinaryTree(1)
two = BinaryTree(2)
three = BinaryTree(3)
four = BinaryTree(4)
five = BinaryTree(5)
six = BinaryTree(6)
seven = BinaryTree(7)
mainTree.left = two
mainTree.right = three
two.left = four
two.right = five
three.left = six
three.right = seven

custDict = treeToLinkedList(mainTree)
print(custDict[3])
print(custDict[2])
print(custDict[1])