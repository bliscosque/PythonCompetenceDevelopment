class BinaryTree:
    def __init__(self, size):
        self.customList=size*[None]
        self.lastUsedIndex=0
        self.maxSize=size

    def insertNode(self,value):
        if self.lastUsedIndex+1==self.maxSize: return "BT is FULL"
        self.customList[self.lastUsedIndex+1]=value
        self.lastUsedIndex+=1
        return "OK"
    
    def searchNode(self,nodeValue):
        for i in range(len(self.customList)):
            if self.customList[i]==nodeValue: return True
        return False

    def preOrderTraversal(self,idx):
        if idx>self.lastUsedIndex: return
        print(self.customList[idx])
        self.preOrderTraversal(idx*2) #left
        self.preOrderTraversal(idx*2+1) #right

    def inOrderTraversal(self,idx):
        if idx>self.lastUsedIndex: return
        self.inOrderTraversal(idx*2) #left
        print(self.customList[idx])
        self.inOrderTraversal(idx*2+1) #right

    def postOrderTraversal(self,idx):
        if idx>self.lastUsedIndex: return
        self.postOrderTraversal(idx*2) #left
        self.postOrderTraversal(idx*2+1) #right  
        print(self.customList[idx])

    def levelOrderTraversal(self,idx):
        for i in range(idx,self.lastUsedIndex+1):
            print(self.customList[i])

    def deleteNode(self,value):
        if self.lastUsedIndex==0: return "No elem"
        for i in range(1,self.lastUsedIndex+1):
            if self.customList[i]==value:
                self.customList[i]=self.customList[self.lastUsedIndex]
                self.customList[self.lastUsedIndex]=None
                self.lastUsedIndex-=1
                return "OK"

    def deleteBT(self):
        self.customList=None

newBT=BinaryTree(8)
newBT.insertNode("Drinks")
newBT.insertNode("Hot")
newBT.insertNode("Cold")
print(newBT.searchNode("Drinks"))
print(newBT.searchNode("Tea"))
newBT.insertNode("Tea")
newBT.insertNode("Coffee")
newBT.preOrderTraversal(1)
print()
newBT.inOrderTraversal(1)
print()
newBT.postOrderTraversal(1)
print()
newBT.levelOrderTraversal(1)
newBT.deleteNode("Tea")
print()
newBT.levelOrderTraversal(1)
