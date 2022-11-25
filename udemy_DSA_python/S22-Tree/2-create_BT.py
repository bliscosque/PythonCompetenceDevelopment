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

class TreeNode:
    def __init__(self, data):
        self.data=data
        self.lChild=None #left
        self.rChild=None #right

    def __str__(self, level=0):
        ret=" "*level+str(self.data) + "\n"
        for child in [self.lChild, self.rChild]:
            if child is not None: ret+=child.__str__(level+1)
        return ret

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

def searchBT(rootNode,nodeValue):
    if not rootNode: return
    else:
        customQueue=Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root=customQueue.dequeue()
            if root.value.data==nodeValue: 
                return "Value exists"
                return
            if root.value.lChild is not None: customQueue.enqueue(root.value.lChild)
            if root.value.rChild is not None: customQueue.enqueue(root.value.rChild)
        return "Value does not exists"
def insertNodeBT(rootNode,newNode):
    if not rootNode: #root node nao existe
        rootNode=newNode
    else:
        customQueue=Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root=customQueue.dequeue()
            if root.value.lChild is not None: customQueue.enqueue(root.value.lChild)
            else: # primeiro posicao livre
                root.value.lChild=newNode
                return "Inserted"
            if root.value.rChild is not None: customQueue.enqueue(root.value.rChild)
            else: # primeiro posicao livre
                root.value.rChild=newNode
                return "Inserted"

def getDeepestNode(rootNode): #usa Level Order Trav
    if not rootNode: return #root node nao existe
    else:
        customQueue=Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root=customQueue.dequeue()            
            if root.value.lChild is not None: customQueue.enqueue(root.value.lChild)
            if root.value.rChild is not None: customQueue.enqueue(root.value.rChild)
        deepestNode=root.value
        return deepestNode

def deleteDeepestNode(rootNode,dNode):
    if not rootNode: return
    else:
        customQueue=Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root=customQueue.dequeue()
            if root.value is dNode:
                root.value=None
                return
            if root.value.rChild is dNode:
                root.value.rChild=None
                return
            else:
                customQueue.enqueue(root.value.rChild)
            if root.value.lChild is dNode:
                root.value.lChild=None
                return
            else:
                customQueue.enqueue(root.value.lChild)

def deleteNodeBT(rootNode, node):
    if not rootNode: return
    else:
        customQueue=Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root=customQueue.dequeue()
            if root.value.data==node:
                dNode=getDeepestNode(rootNode)
                root.value.data=dNode.data
                deleteDeepestNode(rootNode, dNode)
                return "OK"
                return
            if (root.value.lChild is not None): customQueue.enqueue(root.value.lChild)
            if (root.value.rChild is not None): customQueue.enqueue(root.value.rChild)
        return "NOK"

def deleteBT(rootNode):
    rootNode.data=None
    rootNode.lChild=None
    rootNode.rChild=None

newBT = TreeNode("Drinks")
leftChild = TreeNode("Hot")
tea = TreeNode("Tea")
coffee = TreeNode("Coffee")
leftChild.lChild = tea
leftChild.rChild = coffee
rightChild = TreeNode("Cold")
newBT.lChild = leftChild
newBT.rChild = rightChild
print(newBT)
preOrderTraversal(newBT)
print()
inOrderTraversal(newBT)
print()
postOrderTraversal(newBT)
print()
levelOrderTraversal(newBT)
print()
print(searchBT(newBT, "Tea"))
print(searchBT(newBT, "Other"))

newNode=TreeNode("Cola")
insertNodeBT(newBT, newNode)
print()
print(newBT)
#deletion
print("DELETION")
print(getDeepestNode(newBT).data)
deepestNode=getDeepestNode(newBT)
deleteDeepestNode(newBT, deepestNode)
print(newBT)
deleteNodeBT(newBT, 'Hot')
print(newBT)
deleteBT(newBT)
print(newBT)