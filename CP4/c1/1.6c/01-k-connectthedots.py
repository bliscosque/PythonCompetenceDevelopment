import fileinput
import copy
values=['0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ']

def drawConvert(draw):
    nDraw=copy.deepcopy(draw)
    l=len(draw)
    c=len(draw[0])
    for i in range(l):
        elem=[]
        for j in range(c):
            if draw[i][j]!='.': elem.append((draw[i][j],j))
        elem.sort()
        #print(elem)
        for idx in range(len(elem)-1):
            if values.index(elem[idx][0])==values.index(elem[idx+1][0])+1:
                for j in range(elem[idx][1]+1, elem[idx+1][0]):
                    if nDraw[i][j]=='.': nDraw[i][j]='-'
    print(nDraw[i])


lines=[]
for line in fileinput.input():
    lines.append(line.rstrip())

lines.append('')
draw=[]
for line in lines:
    if line=='':
        #proximo desenho

        drawConvert(draw)

        draw=[]
    else:
        draw.append([c for c in line])

