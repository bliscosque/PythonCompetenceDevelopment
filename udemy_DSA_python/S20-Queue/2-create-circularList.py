class Queue:
    def __init__(self, maxSize):
        self.items=maxSize*[None]
        self.maxSize=maxSize
        self.start=-1
        self.top=-1

    def __str__(self):
        values=[str(x) for x in self.items]
        return ' '.join(values)

    def isFull(self):
        if self.top+1==self.start:
            return True
        elif self.start==0 and self.top+1==self.maxSize:
            return True
        else:
            return False
    def isEmpty(self):
        if self.top==-1:
            return True
        else:
            return False
    

    def enqueue(self,value):
        if self.isFull(): return "Queue is FULL"
        else:
            if self.top+1==self.maxSize:
                self.top=0
            else:
                self.top+=1
                if self.start==-1:
                    self.start=0
            self.items[self.top]=value

    def dequeue(self):
        if self.isEmpty(): return "No elem"
        else:
            firstElem=self.items[self.start]
            start=self.start
            if self.start==self.top:
                self.start=-1
                self.top=-1
            elif self.start+1==self.maxSize:
                self.start=0
            else:
                self.start += 1
            self.items[start]=None
            return firstElem

    def peek(self):
        if self.isEmpty(): return "No elem"
        else:
            return self.items[self.start]
    
    def delete(self):
        self.items=self.maxSize*[None]
        self.start=-1
        self.top=-1

customQueue=Queue(3)
print(customQueue.isFull())
print(customQueue.isEmpty())
customQueue.enqueue(1)
customQueue.enqueue(2)
customQueue.enqueue(3)
print(customQueue)
print(customQueue.isFull())
print(customQueue.dequeue())
print(customQueue)
customQueue.enqueue(4)
print(customQueue)
print(customQueue.peek())
customQueue.delete()
print(customQueue)