# Partition a LL around a value x, nodes less than x come b4 nodes greater or equal x
from LL_class import LL

def partition(ll, x):
    curNode=ll.head
    ll.tail=ll.head

    while curNode:
        nextNode=curNode.next
        curNode.next=None
        if curNode.value<x:
            curNode.next=ll.head
            ll.head=curNode
        else:
            ll.tail.next=curNode
            ll.tail=curNode
        curNode=nextNode
    if ll.tail.next is not None:
        ll.tail.next=None

custLL = LL()
custLL.generate(10,0,99)
print(custLL)
partition(custLL,30)
print(custLL)