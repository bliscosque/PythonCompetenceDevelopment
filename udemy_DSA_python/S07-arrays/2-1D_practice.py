from array import *

#1. Create an array and traverse
print("# 1")
my_array=array('i', [1,2,3,4,5])
for i in my_array:
    print(i)

#2. Access individual elem through indexes
print("# 2")
print(my_array[0])

#3. Insert value in an array using append()
print("# 3")
my_array.append(6)
print(my_array)

#4. Insert value in an array using insert()
print("# 4")
my_array.insert(0,0) 
print(my_array)

#5. Extend python array using extend()
print("# 5")
my_array1=array('i',[10,11,12])
my_array.extend(my_array1)
print(my_array)

#6. Add items from list into array using fromlist()
print("# 6")
tmpList=[20,21,22]
my_array.fromlist(tmpList)
print(my_array)

#7. Remove any array elem using remove() # REMOVE PRIMEIRA OCORRENCIA!!!
print("# 7")
my_array.remove(20)
print(my_array)

#8. Remove last elem using pop()
print("# 8")
print(my_array.pop())
print(my_array)

#9. Fetch elem through its index using index()
print("# 9")
print(my_array.index(21))

#10. Reverse a python array using reverse()
print("# 10")
my_array.reverse()
print(my_array)

#11. Get array buffer information through buffer_info()
print("# 11")
print(my_array.buffer_info()) #start point in memory and # os elem

#12. Number of ocurrences of an elem using count()
print("# 12")
print(my_array.count(11))
print(my_array.count(-1))

#13. Convert array to string using toString() - depracated - new is tobytes/frombytes
print("# 13")
strTemp=my_array.tobytes()
print(strTemp)
ints=array('i')
ints.frombytes(strTemp)
print(ints)

#14. Convert array to python list with same elem using toList()
print("# 14")
print(my_array.tolist())

#15. Slice elem from an array
print("# 15")
print(my_array[0:3])