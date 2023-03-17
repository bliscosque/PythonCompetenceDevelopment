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

sll = SLL()
# insert at head
sll.insertSLL(4, 0) # value,location
sll.insertSLL(3, 0) # value,location
sll.insertSLL(2, 0) # value,location
sll.insertSLL(1, 0) # value,location
sll.insertSLL(0, 0) # value,location
print([node.value for node in sll])