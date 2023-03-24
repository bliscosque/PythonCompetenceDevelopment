def catAndMouse(x, y, z):
    if abs(x-z)<abs(y-z):
        return 'Cat A'
    elif abs(x-z)>abs(y-z):  
        return 'Cat B'
    else:
        return 'Mouse C'

catAndMouse(2,5,4)
catAndMouse(1,3,2)