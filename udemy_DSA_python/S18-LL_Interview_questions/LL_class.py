from random import randint
class Node:
    def __init__(self, value=None):
        self.value=value
        self.next=None
        self.prev=None

    def __str__(self) -> str:
        return str(self.value)

class LL:
    def __init__(self, value=None) -> None:
        self.head=None
        self.tail=None

    def __iter__(self):
        curNone=self.head
        while curNone:
            yield curNone
            curNone=curNone.next

    def __str__(self) -> str:
        values=[str(x.value) for x in self]
        return ' -> '.join(values)

    def __len__(self):
        result=0
        node=self.head
        while node:
            result+=1
            node=node.next
        return result

    def add(self, value):
        if self.head is None:
            newNode=Node(value)
            self.head=newNode
            self.tail=newNode
        else:
            self.tail.next=Node(value)
            self.tail=self.tail.next
        return self.tail

    def generate(self,n,min_value,max_value):
        self.head=None
        self.tail=None
        for i in range(n):
            self.add(randint(min_value, max_value))
        return self

#custLL=LL()
#custLL.generate(10,0,99)
#print(custLL)
#print(len(custLL))