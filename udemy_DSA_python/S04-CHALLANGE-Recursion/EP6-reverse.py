#Write a recursive function called reverse which accepts a string and returns a new string in reverse.

def reverse(str): 
    if len(str)<=1: return str
    else: return str[-1]+reverse(str[1:-1])+str[0]


print(reverse('python')) # 'nohtyp'
print(reverse('appmillers')) # 'srellimppa'