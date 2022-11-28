# Write a function called middle that takes a list and returns a new list that contains all but the first and last elements.

myList = [1, 2, 3, 4]


def middle(lst):
    return lst[1:-1]

print(middle(myList))  # [2,3]