class Heap:
    def __init__(self, size) -> None:
        self.customList=(size+1)*[None]
        self.heapSize=0
        self.maxSize=size+1
def peekOfHeap(rootNode):
    if not rootNode: return
    else: return rootNode.customList[1]
def sizeOfHeap(rootNode):
    if not rootNode: return
    else: return rootNode.heapSize
def levelOrderTraversal(rootNode):
    if not rootNode: return
    else:
        for i in range(1,rootNode.heapSize+1):
            print(rootNode.customList[i])
def heapifyTreeInsert(rootNode, idx, heapType):
    parentIndex=idx//2
    if idx <=1: return
    if heapType=="Min":
        if rootNode.customList[idx] < rootNode.customList[parentIndex]:
            rootNode.customList[idx], rootNode.customList[parentIndex] = rootNode.customList[parentIndex], rootNode.customList[idx]
        heapifyTreeInsert(rootNode,parentIndex, heapType)
    elif heapType=="Max":
        if rootNode.customList[idx] > rootNode.customList[parentIndex]:
            rootNode.customList[idx], rootNode.customList[parentIndex] = rootNode.customList[parentIndex], rootNode.customList[idx]
        heapifyTreeInsert(rootNode,parentIndex, heapType)
def insertNode(rootNode, nodeValue, heapType):
    if rootNode.heapSize+1==rootNode.maxSize:
        return "BH is full"
    rootNode.customList[rootNode.heapSize+1]=nodeValue
    rootNode.heapSize+=1
    heapifyTreeInsert(rootNode,rootNode.heapSize, heapType)
def heapifyTreeExtract(rootNode, idx, heapType):
    lIdx=idx*2 #left child
    rIdx=idx*2+1 # right child
    swapChild=0
    if rootNode.heapSize<lIdx: return
    elif rootNode.heapSize==lIdx: #have only leftChild
        if heapType=="Min":
            if rootNode.customList[idx] > rootNode.customList[lIdx]:
                rootNode.customList[idx], rootNode.customList[lIdx] = rootNode.customList[lIdx], rootNode.customList[idx]
            return
        else:
            if rootNode.customList[idx] < rootNode.customList[lIdx]:
                rootNode.customList[idx], rootNode.customList[lIdx] = rootNode.customList[lIdx], rootNode.customList[idx]
            return
    else: # 2 children
        if heapType=="Min":
            if rootNode.customList[lIdx] < rootNode.customList[rIdx]: swapChild=lIdx
            else: swapChild=rIdx
            if rootNode.customList[idx] > rootNode.customList[swapChild]:
                rootNode.customList[idx], rootNode.customList[swapChild] = rootNode.customList[swapChild], rootNode.customList[idx]
        else:
            if rootNode.customList[lIdx] > rootNode.customList[rIdx]: swapChild=lIdx
            else: swapChild=rIdx
            if rootNode.customList[idx] < rootNode.customList[swapChild]:
                rootNode.customList[idx], rootNode.customList[swapChild] = rootNode.customList[swapChild], rootNode.customList[idx]
    heapifyTreeExtract(rootNode, swapChild, heapType)

def extractNode(rootNode, heapType):
    if rootNode.heapSize==0: return
    else: 
        extractedNode=rootNode.customList[1]
        rootNode.customList[1]=rootNode.customList[rootNode.heapSize]
        rootNode.customList[rootNode.heapSize]=None
        rootNode.heapSize-=1
        heapifyTreeExtract(rootNode, 1, heapType)
        return extractedNode
def deleteEntireBH(rootNode):
    rootNode.customList=None

newBH=Heap(5)
insertNode(newBH, 4, "Max")
insertNode(newBH, 5, "Max")
insertNode(newBH, 2, "Max")
insertNode(newBH, 1, "Max")
print()
print(extractNode(newBH, "Max"))
print()
levelOrderTraversal(newBH)
print()
print(sizeOfHeap(newBH))
deleteEntireBH(newBH)
#levelOrderTraversal(newBH)