class Node:
    def __init__(self, value=None):
        self.value=value
        self.next=None

class SLL:
    def __init__(self):
        self.head=None
        self.tail=None
    def __iter__(self):
        node=self.head
        while node:
            yield node
            node=node.next
    def insertSLL(self,value,location):
        newNode=Node(value)
        if self.head is None: # primeiro no da lista
            self.head=newNode
            self.tail=newNode
        else:
            if location==0: # inicio da lista
                newNode.next=self.head
                self.head=newNode
            elif location==-1: # fim da lista
                newNode.next=None
                self.tail.next=newNode
                self.tail=newNode
            else: # meio da lista
                tempNode=self.head
                idx=0
                while idx<location-1: 
                    tempNode=tempNode.next
                    idx+=1
                nextNode=tempNode.next
                tempNode.next=newNode
                newNode.next=nextNode
    def traverseSLL(self):
        if self.head is None:
            print("SLL is empty")
        else:
            node=self.head
            while node is not None:
                print(node.value)
                node=node.next
    def searchSLL(self, nodeValue):
        if self.head is None:
            return "SLL is empty"
        else:
            node=self.head
            while node is not None:
                if node.value==nodeValue: return node.value
                node=node.next
            return "Value does not exists in list"

    def deleteNodeSLL(self,location):
        if self.head is None:
            print("SLL is empty")
        else:
            if location==0: # primeiro no
                if self.head==self.tail: # temos apenas 1 no
                    self.head=None
                    self.tail=None
                else: # mais de um nó
                    self.head=self.head.next
            elif location==-1:
                if self.head==self.tail: # temos apenas 1 no
                    self.head=None
                    self.tail=None
                else: # mais de um nó
                    node=self.head
                    while node is not None:
                        if node.next == self.tail: break
                        node=node.next
                    node.next=None
                    self.tail=node
            else:
                tempNode=self.head
                idx=0
                while idx < location-1:
                    tempNode=tempNode.next
                    idx+=1
                nextNode=tempNode.next
                tempNode.next=nextNode.next
                    

sll = SLL()
sll.insertSLL(2, -1)
sll.insertSLL(3, -1)
sll.insertSLL(4, -1)
sll.insertSLL(0, 0)
sll.insertSLL(0, 3)

print([node.value for node in sll])
#sll.traverseSLL()
#print(sll.searchSLL(3))
#print(sll.searchSLL(33))
sll.deleteNodeSLL(0)
print([node.value for node in sll])
sll.deleteNodeSLL(-1)
print([node.value for node in sll])
sll.deleteNodeSLL(1)
print([node.value for node in sll])