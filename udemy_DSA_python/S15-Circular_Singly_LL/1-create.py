class Node:
    def __init__(self, value=None):
        self.value=value
        self.next=None

class CSLL:
    def __init__(self):
        self.head=None
        self.tail=None
    def __iter__(self):
        node=self.head
        while node:
            yield node
            if node.next==self.head: break # chegou ao head novamente
            node=node.next


    def createCSLL(self, nodeValue):
        node = Node(nodeValue)
        node.next=node
        self.head=node
        self.tail=node
        return "CSLL has been created"

    def insertCSLL(self, value, location):
        if self.head is None:
            return "Head is None"
        else:
            newNode = Node(value)
            if location==0:
                newNode.next=self.head
                self.head=newNode
                self.tail.next=newNode
            elif location==-1:
                newNode.next=self.tail.next
                self.tail.next=newNode
                self.tail=newNode
            else:
                tmpNode=self.head
                idx=0
                while idx< location-1:
                    tmpNode=tmpNode.next
                    idx+=1
                nextNode=tmpNode.next
                tmpNode.next=newNode
                newNode.next=nextNode
            return "Node inserted"

csll = CSLL()
csll.createCSLL(1)
csll.insertCSLL(0, 0)
csll.insertCSLL(-1, 0)
csll.insertCSLL('p1', 1)
csll.insertCSLL('pend', -1)


print([node.value for node in csll])