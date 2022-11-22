#Write a recursive function called capitalizeFirst. Given an array of strings, capitalize the first letter of each string in the array.

def capitalizeFirst(arr):
    if len(arr)==0: return []
    ans=[]
    ans.append(arr[0].capitalize())
    return ans+capitalizeFirst(arr[1:])


print(capitalizeFirst(['car', 'taco', 'banana'])) # ['Car','Taco','Banana']