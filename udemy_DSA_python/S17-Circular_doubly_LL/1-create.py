class Node:
    def __init__(self, value=None):
        self.value=value
        self.next=None
        self.prev=None

class CircularDoublyLL:
    def __init__(self) -> None:
        self.head=None
        self.tail=None
    
    def __iter__(self):
        node=self.head
        while node:
            yield node
            node=node.next
            if node==self.tail.next: break
    
    def createCDLL(self, nodeValue):
        newNode=Node(nodeValue)
        self.head=newNode
        self.tail=newNode
        newNode.prev=newNode
        newNode.next=newNode
        return "OK"

    def insertCDLL(self, value, location):
        if self.head is None: "Empty CDLL"
        else:
            newNode=Node(value)
            if location==0: #inicio
                newNode.next=self.head
                newNode.prev=self.tail
                self.head.prev=newNode
                self.head=newNode
                self.tail.next=newNode
            elif location==-1: #fim
                newNode.next=self.head
                newNode.prev=self.tail
                self.head.prev=newNode
                self.tail.next=newNode
                self.tail=newNode
            else:
                tmpNode=self.head
                idx=0
                while idx < location-1:
                    tmpNode=tmpNode.next
                    idx+=1
                newNode.next=tmpNode.next
                newNode.prev=tmpNode
                newNode.next.prev=newNode
                tmpNode.next=newNode
            return "OK"

    def traversalCDLL(self):
        if self.head is None: print ("No node in CDLL")
        else:
            tmpNode=self.head
            while tmpNode:
                print(tmpNode.value)
                if tmpNode==self.tail: break
                tmpNode=tmpNode.next
    def reverseTraversalCDLL(self):
        if self.head is None: print ("No node in CDLL")
        else:
            tmpNode=self.tail
            while tmpNode:
                print(tmpNode.value)
                if tmpNode==self.head: break
                tmpNode=tmpNode.prev

circDLL = CircularDoublyLL()
circDLL.createCDLL(5)
print([node.value for node in circDLL])
circDLL.insertCDLL(0,0)
circDLL.insertCDLL(99,-1)
circDLL.insertCDLL(2,1)
print([node.value for node in circDLL])
circDLL.traversalCDLL()
circDLL.reverseTraversalCDLL()