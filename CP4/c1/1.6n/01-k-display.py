nums=[]
nums.append("""+---+
|   |
|   |
+   +
|   |
|   |
+---+""".split('\n'))
nums.append("""    +
    |
    |
    +
    |
    |
    +""".split('\n'))
nums.append("""+---+
    |
    |
+---+
|    
|    
+---+""".split('\n'))
nums.append("""+---+
    |
    |
+---+
    |
    |
+---+""".split('\n'))
nums.append("""+   +
|   |
|   |
+---+
    |
    |
    +""".split('\n'))
nums.append("""+---+
|    
|    
+---+
    |
    |
+---+""".split('\n'))
nums.append("""+---+
|    
|    
+---+
|   |
|   |
+---+""".split('\n'))
nums.append("""+---+
    |
    |
    +
    |
    |
    +""".split('\n'))
nums.append("""+---+
|   |
|   |
+---+
|   |
|   |
+---+""".split('\n'))
nums.append("""+---+
|   |
|   |
+---+
    |
    |
+---+""".split('\n'))
nums.append(""" 
 
o
 
o
 
 """.split('\n'))

s=input()
while s.rstrip()!='end':
    hh,min=s.split(":")
    h1=int(hh[0])
    h2=int(hh[1])
    m1=int(min[0])
    m2=int(min[1])
    #print(h1, h2)
    for i in range(7):
        print(f'{nums[h1][i]}  {nums[h2][i]}  {nums[10][i]}  {nums[m1][i]}  {nums[m2][i]}')
    print()
    print()
    s=input()
print("end")