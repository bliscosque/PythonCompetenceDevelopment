class Node:
    def __init__(self, value=None):
        self.value=value
        self.next=None
        self.prev=None

class DoublyLL:
    def __init__(self):
        self.head=None
        self.tail=None
    
    def __iter__(self):
        node=self.head
        while node:
            yield node
            node=node.next
    
    def createSLL(self,nodeValue):
        node=Node(nodeValue)
        node.prev=None
        node.next=None
        self.head=node
        self.tail=node
        return "DLL created"

    def insertNode(self,nodeValue, location):
        if self.head is None:
            print("Node cannot be inserted")
        else:
            newNode=Node(nodeValue)
            if location==0:
                newNode.prev=None
                newNode.next=self.head
                self.head.prev=newNode
                self.head=newNode
            elif location==-1:
                newNode.next=None
                newNode.prev=self.tail
                self.tail.next=newNode
                self.tail=newNode
            else:
                tmpNode=self.head
                idx=0
                while idx<location-1:
                    tmpNode=tmpNode.next
                    idx+=1
                newNode.next=tmpNode.next
                newNode.prev=tmpNode
                newNode.next.prev=newNode
                tmpNode.next=newNode

doublyLL=DoublyLL()
doublyLL.createSLL(5)
print([node.value for node in doublyLL])
doublyLL.insertNode(0, 0)
doublyLL.insertNode(2, -1)
doublyLL.insertNode(1, 1)
print([node.value for node in doublyLL])