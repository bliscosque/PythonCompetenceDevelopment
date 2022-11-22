#Write a recursive function called flatten which accepts an array of arrays and returns a new array with all values flattened.



def flatten(arr):
    ans=[]
    if len(arr)==0: return
    for el in arr:
        if type(el) is list: ans.extend(flatten(el))
        else: ans.append(el)
    return ans
    

print(flatten([1, 2, 3, [4, 5]])) # [1, 2, 3, 4, 5]
print(flatten([1, [2, [3, 4], [[5]]]])) # [1, 2, 3, 4, 5]
print(flatten([[1], [2], [3]])) # [1, 2, 3]
print(flatten([[[[1], [[[2]]], [[[[[[[3]]]]]]]]]])) # [1, 2, 3]