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

    def traverseDLL(self):
        if self.head is None:
            print("No elem")
        else:
            tmpNode=self.head
            while tmpNode:
                print(tmpNode.value)
                tmpNode=tmpNode.next

    def reverseTraverseDLL(self):
        if self.head is None:
            print("No elem")
        else:
            tmpNode=self.tail
            while tmpNode:
                print(tmpNode.value)
                tmpNode=tmpNode.prev

    def search(self, value):
        if self.head is None:
            print("No elem")
        else:
            tmpNode=self.head
            while tmpNode:
                if tmpNode.value==value: return tmpNode.value
                tmpNode=tmpNode.next
            return "Not find in list"

    def deleteDLL(self,location):
        if self.head is None:
            print("No elem")
        else:
            if location==0:
                if self.head==self.tail: #1 elem
                    self.head=None
                    self.tail=None
                else:
                    self.head=self.head.next
                    self.head.prev=None
            elif location==-1: #last node
                if self.head==self.tail: #1 elem
                    self.head=None
                    self.tail=None
                else:
                    self.tail=self.tail.prev
                    self.tail.next=None
            else:
                tmpNode=self.head
                idx=0
                while idx<location-1:
                    tmpNode=tmpNode.next
                    idx+=1
                tmpNode.next=tmpNode.next.next
                tmpNode.next.prev=tmpNode
    def deleteEntireDLL(self):
        if self.head is None:
            print("No elem")
        else:
            tmpNode=self.head
            while tmpNode:
                tmpNode.prev=None
                tmpNode=tmpNode.next
            self.head=None
            self.tail=None


doublyLL=DoublyLL()
doublyLL.createSLL(5)
print([node.value for node in doublyLL])
doublyLL.insertNode(0, 0)
doublyLL.insertNode(2, -1)
doublyLL.insertNode(1, 1)
print([node.value for node in doublyLL])
doublyLL.traverseDLL()
doublyLL.reverseTraverseDLL()
print(doublyLL.search(5))
print(doublyLL.search(99))
print()
print([node.value for node in doublyLL])
doublyLL.deleteDLL(0)
print([node.value for node in doublyLL])
doublyLL.deleteDLL(1)
print([node.value for node in doublyLL])
doublyLL.deleteDLL(-1)
print([node.value for node in doublyLL])
doublyLL.deleteEntireDLL()
print([node.value for node in doublyLL])
