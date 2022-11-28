#Given a list, write a function to get first, second best scores from the list.
#List may contain duplicates.

def firstSecond(givenList):
    lst2=list(set(givenList))
    lst2.sort()
    print(lst2[-1], lst2[-2])

myList = [84,85,86,87,85,90,85,83,23,45,84,1,2,0]
firstSecond(myList)