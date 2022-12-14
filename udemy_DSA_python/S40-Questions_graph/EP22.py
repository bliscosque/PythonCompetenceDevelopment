# Given a sorted (increasing order) array with unique integer elements, write an algorithm to create a binary search tree 
# with minimal height.

class BSTNode:
    def __init__(self, data=None, left = None, right= None):
        self.data = data
        self.left = left
        self.right = right

def preOrderTraversal(rootNode):
    if not rootNode: return
    print(rootNode.data)
    preOrderTraversal(rootNode.left)
    preOrderTraversal(rootNode.right)

def minimalTreeHelper(root,arr):
    if len(arr)==0: return None
    mid=len(arr)//2
    root=BSTNode(arr[mid])
    root.left=minimalTreeHelper(root.left,arr[:mid])
    root.right=minimalTreeHelper(arr,arr[mid+1:])
    return root


def minimalTree(sortedArray):
    return minimalTreeHelper(BSTNode(),sortedArray)
    

sortedArray = [1,2,3,4,5,6,7,8,9]
root=minimalTree(sortedArray)
preOrderTraversal(root)
#Output
#   _5__  
#  /    \ 
#  3    8 
# / \  / \
# 2 4  7 9
#/    /   
#1    6 