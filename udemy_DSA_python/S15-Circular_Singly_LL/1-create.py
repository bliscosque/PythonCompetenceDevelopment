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
    def traverseCSLL(self):
        if self.head is None:
            print("CSLL is empty")
        else:
            node=self.head
            while node:
                print(node.value)
                node=node.next
                if node==self.tail.next: break # chegou ao fim
    def searchCSLL(self, nodeValue):
        if self.head is None:
            return "CSLL is empty"
        else:
            node=self.head
            while node:
                if node.value==nodeValue: return node.value
                node=node.next
                if node==self.tail.next: break # chegou ao fim
            return "Value does not exists in list"
    def deleteNodeCSLL(self,location):
        if self.head is None:
            print("CSLL is empty")
        else:
            if location==0: # primeiro no
                if self.head==self.tail: # temos apenas 1 no
                    self.head.next=None
                    self.head=None
                    self.tail=None
                else: # mais de um nó
                    self.head=self.head.next
                    self.tail.next=self.head
            elif location==-1: #deletar no final
                if self.head==self.tail: # temos apenas 1 no
                    self.head.next=None
                    self.head=None
                    self.tail=None
                else: # mais de um nó
                    node=self.head
                    while node is not None:
                        if node.next == self.tail: break
                        node=node.next
                    node.next=self.head
                    self.tail=node
            else:
                tempNode=self.head
                idx=0
                while idx < location-1:
                    tempNode=tempNode.next
                    idx+=1
                nextNode=tempNode.next
                tempNode.next=nextNode.next

    def deleteEntireCSLL(self):
        if self.head is None:
            print("CSLL is empty")
        else:
            self.head=None
            self.tail.next=None
            self.tail=None

csll = CSLL()
csll.createCSLL(1)
csll.insertCSLL(0, 0)
csll.insertCSLL(-1, 0)
csll.insertCSLL('p1', 1)
csll.insertCSLL('pend', -1)
csll.traverseCSLL()
print("###")
print(csll.searchCSLL('pend'))
print(csll.searchCSLL(1))
print(csll.searchCSLL(99))

print([node.value for node in csll])
#csll.traverseCSLL()
csll.deleteNodeCSLL(-1)
csll.deleteNodeCSLL(1)
csll.deleteNodeCSLL(0)
print([node.value for node in csll])

csll.deleteEntireCSLL()
print([node.value for node in csll])