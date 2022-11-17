#Write a function called productOfArray which takes in an array of numbers and returns the product of them all.

def productOfArray(arr):
    if len(arr)==0: return 1
    elif len(arr)==1: return arr[0]
    return arr[0]*productOfArray(arr[1:])

print(productOfArray([1,2,3])) #6
print(productOfArray([1,2,3,10])) #60