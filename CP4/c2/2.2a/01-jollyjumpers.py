import fileinput
lines=[]
for line in fileinput.input():
	lines.append(line.rstrip()) #remove o '\r'
for line in lines:
    a=[int(i) for i in line.split()]
    b=set()
    for i in range(1,len(a)-1):
         b.add(i)
    #print(b)
    if len(a)>1:
        for i in range(len(a)-1,0,-1):
            el=abs(a[i]-a[i-1])
            if el in b: b.remove(el)
    if len(b)==0:
        print("Jolly")
    else:
        print("Not jolly")


                