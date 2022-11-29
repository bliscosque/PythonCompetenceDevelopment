# Classes auxiliares
class Node:
    def __init__(self, value=None):
        self.value=value
        self.next=None

    def __str__(self):
        return str(self.value)
class SLL:
    def __init__(self):
        self.head=None
        self.tail=None

    def __iter__(self):
        node=self.head
        while node:
            yield node
            node=node.next
class Queue:
    def __init__(self):
        self.ll=SLL()

    def __str__(self):
        values=[str(x) for x in self.ll]
        return ' '.join(values)

    def enqueue(self,value):
        newNode=Node(value)
        if self.ll.head is None: # primeiro no da lista
            self.ll.head=newNode
            self.ll.tail=newNode
        else:
            self.ll.tail.next=newNode
            self.ll.tail=newNode
    
    def isEmpty(self):
        return self.ll.head == None

    def dequeue(self):
        if self.isEmpty(): "No elem"
        else:
            tmpNode=self.ll.head
            if self.ll.head == self.ll.tail: # 1 elem
                self.ll.head=None
                self.ll.tail=None
            else:
                self.ll.head=self.ll.head.next
            return tmpNode

    def peek(self):
        if self.isEmpty(): "No elem"
        else:
            return self.ll.head

    def delete(self):
        self.ll.head=None
        self.ll.tail=None

# Classe principal deste módulo

class AVLNode:
    def __init__(self, data):
        self.data=data
        self.lChild=None
        self.rChild=None
        self.height=1

def preOrderTraversal(rootNode):
    if not rootNode: return
    print(rootNode.data)
    preOrderTraversal(rootNode.lChild)
    preOrderTraversal(rootNode.rChild)
        
def inOrderTraversal(rootNode):
    if not rootNode: return
    inOrderTraversal(rootNode.lChild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rChild)
    
def postOrderTraversal(rootNode):
    if not rootNode: return
    postOrderTraversal(rootNode.lChild)
    postOrderTraversal(rootNode.rChild)
    print(rootNode.data)

def levelOrderTraversal(rootNode):
    if not rootNode: return
    else:
        customQueue=Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root=customQueue.dequeue()
            print(root.value.data)
            if (root.value.lChild is not None): customQueue.enqueue(root.value.lChild)
            if (root.value.rChild is not None): customQueue.enqueue(root.value.rChild)

def searchNode(rootNode,nodeValue):
    if rootNode.data==nodeValue: print("found")
    elif nodeValue < rootNode.data:
        if rootNode.lChild.data==nodeValue:
            print("Found")
        else: searchNode(rootNode.lChild,nodeValue)
    else:
        if rootNode.rChild.data==nodeValue:
            print("Found")
        else: searchNode(rootNode.rChild,nodeValue)

def getHeight(rootNode):
    if not rootNode: return 0
    return rootNode.height

def rightRotate(disbNode):
    newRoot=disbNode.lChild
    disbNode.lChild=disbNode.lChild.rChild
    newRoot.rChild=disbNode
    disbNode.height = 1+max(getHeight(disbNode.lChild), getHeight(disbNode.rChild))
    newRoot.height = 1+max(getHeight(newRoot.lChild), getHeight(newRoot.rChild))
    return newRoot

def leftRotate(disbNode):
    newRoot=disbNode.rChild
    disbNode.rChild=disbNode.rChild.lChild
    newRoot.lChild=disbNode
    disbNode.height = 1+max(getHeight(disbNode.lChild), getHeight(disbNode.rChild))
    newRoot.height = 1+max(getHeight(newRoot.lChild), getHeight(newRoot.rChild))
    return newRoot    

def getBalance(rootNode):
    if not rootNode: return 0
    return getHeight(rootNode.lChild) - getHeight(rootNode.rChild)

def insertNode(rootNode, nodeValue):
    if not rootNode:
        return AVLNode(nodeValue)
    elif nodeValue < rootNode.data:
        rootNode.lChild = insertNode(rootNode.lChild, nodeValue)
    else:
        rootNode.rChild = insertNode(rootNode.rChild, nodeValue)

    rootNode.height=1+max(getHeight(rootNode.lChild), getHeight(rootNode.rChild))
    balance=getBalance(rootNode)
    if balance > 1 and nodeValue < rootNode.lChild.data: # LL
        return rightRotate(rootNode)
    if balance > 1 and nodeValue > rootNode.lChild.data: # LR
        rootNode.lChild=leftRotate(rootNode.lChild) 
        return rightRotate(rootNode)
    if balance < -1 and nodeValue > rootNode.rChild.data: # RR
        return leftRotate(rootNode)
    if balance < -1 and nodeValue < rootNode.rChild.data: # RL
        rootNode.rChild = rightRotate(rootNode.rChild)
        leftRotate(rootNode)
    return rootNode

def deleteAVL(rootNode):
    rootNode.data=None
    rootNode.lChild=None
    rootNode.rChild=None
    return "OK"

newAVL=AVLNode(5)
newAVL=insertNode(newAVL, 10)
newAVL=insertNode(newAVL, 15)
newAVL=insertNode(newAVL, 20)
levelOrderTraversal(newAVL)