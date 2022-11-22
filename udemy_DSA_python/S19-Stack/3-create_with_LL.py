class Node:
    def __init__(self, value=None):
        self.value=value
        self.next=None

class LL:
    def __init__(self):
        self.head=None

    def __iter__(self):
        node=self.head
        while node:
            yield node
            node=node.next

class Stack:
    def __init__(self):
        self.ll=LL()

    def __str__(self):
        values=[str(x.value) for x in self.ll]
        return '\n'.join(values)

    def isEmpty(self):
        if self.ll.head==None:
            return True
        return False

    def push(self,value):
        node=Node(value)
        node.next=self.ll.head
        self.ll.head=node

    def pop(self):
        if self.isEmpty(): return "is Empty"
        else:
            nodeValue=self.ll.head.value
            self.ll.head=self.ll.head.next
            return nodeValue

    def peek(self):
        if self.isEmpty(): return "is Empty"
        else:
            nodeValue=self.ll.head.value
            return nodeValue

    def delete(self):
        self.ll.head=None

customStack=Stack()
print(customStack.isEmpty())
customStack.push(1)
customStack.push(2)
customStack.push(3)
print(customStack)
print()
print(customStack.pop())
print()
print(customStack)
print(customStack.peek())
