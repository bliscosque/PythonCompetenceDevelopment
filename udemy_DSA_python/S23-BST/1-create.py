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

class BSTNode:
    def __init__(self, data):
        self.data=data
        self.lChild=None
        self.rChild=None

def insertNode(rootNode,nodeValue):
    if rootNode.data==None: rootNode.data=nodeValue
    elif nodeValue<=rootNode.data: # menor, está a esquerda
        if rootNode.lChild is None: # 1 nó
            rootNode.lChild=BSTNode(nodeValue)
        else: #chamada recursiva
            insertNode(rootNode.lChild,nodeValue)
    else: # maior, a direita
        if rootNode.rChild is None: # 1 nó
            rootNode.rChild=BSTNode(nodeValue)
        else: #chamada recursiva
            insertNode(rootNode.rChild,nodeValue)

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

def minValue(bstNode):
    current=bstNode
    while (current.lChild is not None):
        current=current.lChild
    return current

def deleteNode(rootNode, nodeValue):
    if rootNode is None:
        return rootNode
    if nodeValue < rootNode.data:
        rootNode.lChild=deleteNode(rootNode.lChild, nodeValue)
    elif nodeValue > rootNode.data:
        rootNode.rChild=deleteNode(rootNode.rChild,nodeValue)
    else: 
        # only 1 child
        if rootNode.lChild is None:
            tmp=rootNode.rChild
            rootNode=None
            return tmp
        if rootNode.rChild is None:
            tmp=rootNode.lChild
            rootNode=None
            return tmp
        # 2 children
        tmp=minValue(rootNode.rChild)
        rootNode.data=tmp.data
        rootNode.rChild=deleteNode(rootNode.rChild, tmp.data)
    return rootNode

def deleteBST(rootNode):
    rootNode.data=None
    rootNode.lChild=None
    rootNode.rChild=None
    return "OK"

newBST=BSTNode(None)
insertNode(newBST, 70)
insertNode(newBST, 50)
insertNode(newBST, 90)
#print(newBST.data, newBST.lChild.data, newBST.rChild.data)
insertNode(newBST, 30)
insertNode(newBST, 60)
insertNode(newBST, 80)
insertNode(newBST, 100)
insertNode(newBST, 20)
insertNode(newBST, 40)
print("pre order")
preOrderTraversal(newBST)
print("in order")
inOrderTraversal(newBST)
print("post order")
postOrderTraversal(newBST)
print("level order")
levelOrderTraversal(newBST)
searchNode(newBST,60)
deleteNode(newBST, 100)
levelOrderTraversal(newBST)
deleteBST(newBST)
levelOrderTraversal(newBST)