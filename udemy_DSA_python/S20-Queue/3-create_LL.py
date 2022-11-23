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

customQueue=Queue()
print(customQueue.isEmpty())
customQueue.enqueue(1)
customQueue.enqueue(2)
customQueue.enqueue(3)
print(customQueue.isEmpty())
print(customQueue)
print(customQueue.dequeue())
print(customQueue.peek())
print(customQueue)