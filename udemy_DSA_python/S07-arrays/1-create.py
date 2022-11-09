from array import *

arr1=array('i',[1,2,3,4,5,6]) #integers array
arr2=array('d',[1.3,1.5,1.6]) #double array
arr1.insert(6,7) #insert pos=6, val=7
arr1.insert(0,0) #insert pos=0, val=0
arr1.insert(100,10) #insert at end, já que nao há 100 elementos
arr1.remove(2)
print(arr1)
print(len(arr1))
print(arr2)