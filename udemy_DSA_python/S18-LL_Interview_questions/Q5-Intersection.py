# check intersection of LL (by reference, not values)

from LL_class import LL, Node

def intersection(llA, llB):
    if llA.tail is not llB.tail: return False # nao há interseccao

    lenA=len(llA)
    lenB=len(llB)

    shorter = llA if lenA < lenB else llB
    longer = llB if lenA < lenB else llA

    diff=len(longer)-len(shorter)
    longerNode=longer.head
    shortNode=shorter.head

    for i in range(diff):
        longerNode=longerNode.next

    while shortNode is not longerNode:
        shortNode=shortNode.next
        longerNode=longerNode.next
    
    return longerNode

#Helper function
def addSameNode(llA, llB, value):
    tmpNode=Node(value)
    llA.tail.next=tmpNode
    llA.tail=tmpNode
    llB.tail.next=tmpNode
    llB.tail=tmpNode

llA=LL()
llA.generate(3,0,10)
llB=LL()
llB.generate(4,11,20)
addSameNode(llA, llB, 30)
addSameNode(llA, llB, 35)
print(llA)
print(llB)
print(intersection(llA, llB))