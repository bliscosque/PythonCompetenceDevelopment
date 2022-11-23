class Queue:
    def __init__(self):
        self.items=[]

    def __str__(self):
        values=[str(x) for x in self.items]
        return ' '.join(values)

    def isEmpty(self):
        return self.items==[]

    def enqueue(self,value):
        self.items.append(value)
    
    def dequeue(self):
        if self.isEmpty():
            return "no elem in queue"
        else:
            return self.items.pop(0)

    def peek(self):
        if self.isEmpty():
            return "no elem in queue"
        else:
            return self.items[0]
    
    def delete(self):
        self.items=[]

customQueue=Queue()
print(customQueue.isEmpty())
customQueue.enqueue(1)
customQueue.enqueue(2)
customQueue.enqueue(3)
print(customQueue)
print(customQueue.dequeue())
print(customQueue)
print(customQueue.peek())
print(customQueue)
customQueue.delete()
print(customQueue)