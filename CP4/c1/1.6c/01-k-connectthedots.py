import fileinput
import copy
values=[ch for ch in '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ']

def drawConvert(draw):
    #print(values)
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
            el=str(elem[idx][0])
            nel=str(elem[idx+1][0])
            #print(el,nel)
            pel=values.index(el)
            pnel=values.index(nel)
            #print(pel,pnel)
            if pel+1==pnel: # ver tbm reverso
                for j in range(elem[idx][1]+1, elem[idx+1][1]):
                    if nDraw[i][j]=='.': nDraw[i][j]='-'
                for j in range(elem[idx][1]-1, elem[idx+1][1],-1):
                    if nDraw[i][j]=='.': nDraw[i][j]='-'

    for j in range(c):
        elem=[]
        for i in range(l):
            if draw[i][j]!='.' and draw[i][j]!='-': elem.append((draw[i][j],i))
        elem.sort()
        #print(elem)
        for idx in range(len(elem)-1):
            el=str(elem[idx][0])
            nel=str(elem[idx+1][0])
            #print(el,nel)
            pel=values.index(el)
            pnel=values.index(nel)
            #print(pel,pnel)
            if pel+1==pnel: # ver tbm reverso
                for i in range(elem[idx][1]+1, elem[idx+1][1]):
                    if nDraw[i][j]=='.': nDraw[i][j]='|'
                    if nDraw[i][j]=='-': nDraw[i][j]='+'
                for i in range(elem[idx][1]-1, elem[idx+1][1],-1):
                    if nDraw[i][j]=='.': nDraw[i][j]='|'
                    if nDraw[i][j]=='-': nDraw[i][j]='+'

    for i in range(l):
        print(''.join(nDraw[i]))
    print()

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

