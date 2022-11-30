from LL_class import LL

def removeDups(ll):
    if ll.head is None: return
    else:
        curNode=ll.head
        visited=set([curNode.value])
        while curNode.next:
            if curNode.next.value in visited: # duplicado
                curNode.next=curNode.next.next
            else:
                visited.add(curNode.next.value)
                curNode=curNode.next
        return ll

customLL = LL()
customLL.generate(10,0,99)
print(customLL)
removeDups(customLL)
print(customLL)