#Write a function to find the duplicate number on given integer array/list.
def removeDuplicates(myList):
    return list(set(myList))

print(removeDuplicates([1, 1, 2, 2, 3, 4, 5]))
#Output : [1, 2, 3, 4, 5]