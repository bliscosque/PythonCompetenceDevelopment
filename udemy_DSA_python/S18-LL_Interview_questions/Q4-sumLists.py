#list1=  7->1->6 (representa 617)
#list2=  5->9->2 (representa 295)
#sumList=2->1->9 (representa 912)

from LL_class import LL

def sumList(llA, llB):
    n1=llA.head
    n2=llB.head
    carry=0
    llSum=LL()
    while n1 or n2:
        result=carry
        if n1:
            result+=n1.value
            n1=n1.next
        if n2:
            result+=n2.value
            n2=n2.next            
        llSum.add(result%10)
        carry = result//10
    return llSum

llA=LL()
llA.add(7)
llA.add(1)
llA.add(6)

llB=LL()
llB.add(5)
llB.add(9)
llB.add(2)
print(llA)
print(llB)
print(sumList(llA,llB))