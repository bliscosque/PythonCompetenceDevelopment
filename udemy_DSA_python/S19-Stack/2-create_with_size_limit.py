class Stack:
    def __init__(self, maxSize):
        self.maxSize=maxSize
        self.list=[]

    def __str__(self):
        values=reversed(self.list)
        values=[str(x) for x in values]
        return '\n'.join(values)

    def isEmpty(self):
        if self.list==[]: return True
        return False

    def isFull(self):
        if len(self.list)==self.maxSize: return True
        return False

    def push(self, value):
        if self.isFull(): return "The stack is full"
        self.list.append(value)
    
    def pop(self):
        if self.isEmpty(): return "No element"
        else:
            return self.list.pop()

    def peek(self):
        if self.isEmpty(): return "No element"
        else: return self.list[len(self.list)-1]

    def delete(self):
        self.list=None

customStack=Stack(4)
print(customStack.isEmpty())
print(customStack.isFull())
customStack.push(1)
customStack.push(2)
customStack.push(3)
print(customStack)
print()