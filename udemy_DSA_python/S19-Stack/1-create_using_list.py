class Stack:
    def __init__(self):
        self.list=[]
    
    def __str__(self):
        values=reversed(self.list)
        values=[str(x) for x in values]
        return '\n'.join(values)

    def isEmpty(self):
        if self.list==[]: return True
        return False

    def push(self, value):
        self.list.append(value)

    def pop(self):
        if self.isEmpty(): return "No element"
        else:
            return self.list.pop()

    def peek(self):
        if self.isEmpty(): return "No element"
        else: return self.list[len(self.list)-1]

customStack=Stack()
print(customStack.isEmpty())
customStack.push(0)
customStack.push(1)
customStack.push(2)
print(customStack)
print()
print(customStack.pop())
print()
print(customStack)
print(customStack.peek())