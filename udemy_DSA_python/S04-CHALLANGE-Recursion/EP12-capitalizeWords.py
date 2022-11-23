#Write a recursive function called capitalizeWords. Given an array of words, return a new array containing each word capitalized.

def capitalizeWords(arr):
    if len(arr)==1: return [arr[0].upper()]
    else: return [arr[0].upper()]+capitalizeWords(arr[1:])

words = ['i', 'am', 'learning', 'recursion']
print(capitalizeWords(words)) # ['I', 'AM', 'LEARNING', 'RECURSION']