def pairSum(arr,sum):
    s=set()
    for el in arr:
        x=sum-el
        if x in s:
            return (x,el)
        s.add(el)
    return (None,None)

arr=[10, 5, 2 , 3, -6, 9 , 11]
print(pairSum(arr,4))