#Implement three stacks using a single list

class MultiStack:
    def __init__(self, stackSize) -> None:
        self.nStacks=3
        self.custList=[0]*stackSize*self.nStacks
        self.sizes=[0]*self.nStacks
        self.stackSize=stackSize

    def isFull(self, stackNum):
        return self.sizes[stackNum]==self.stackSize
    
    def isEmpty(self,stackNum):
        return self.sizes[stackNum]==0
    
    def idxTop(self, stackNum):
        offset=stackNum*self.stackSize
        return offset*self.sizes[stackNum]-1

    def push(self, item, stackNum):
        if self.isFull(stackNum): return "Stack full"
        self.sizes[stackNum]+=1
        self.custList[self.idxTop(stackNum)]=item
    
    def pop(self, stackNum):
        if self.isEmpty(stackNum): return "stack empty"
        value=self.custList[self.idxTop(stackNum)]
        self.sizes[stackNum]-=1
        return value

    def peek(self, stackNum):
        if self.isEmpty(stackNum): return "stack empty"
        value=self.custList[self.idxTop(stackNum)]
        return value

customStack=MultiStack(6)
print(customStack.isFull(0))
print(customStack.isEmpty(1))
customStack.push(1, 0)
customStack.push(2, 0)
customStack.push(3, 2)
print(customStack.peek(0))
print(customStack.pop(0))