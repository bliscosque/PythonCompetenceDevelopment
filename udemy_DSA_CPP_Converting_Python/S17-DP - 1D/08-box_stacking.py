# given arr of boxes. Each box represented with 3 int (depth,width,heigh).
# Goal: maximise the total height of the stack.
# Can't rotate any box and each box must have strictly smaller width,depth and height than box below.

# idea: fazer um sort baseado na altura (ultimo campo)
# para cada caixa, verificar as caixas ate ali que podem ser colocados sobre elas. Alguma das caixas anteriores ja estarao calculadas (DP)

def box_stack(boxes):
    n=len(boxes)
    b=sorted(boxes,key=lambda x:x[2]) # ordena com base ultimo campo
    h=[0]*n
    for i in range(n):
        h[i]=b[i][2]
    for i in range(1,n):
        for j in range(i):
            if b[i] > b[j]:
                #print(b[i][2], h[j])
                h[i]=max(h[i],b[i][2]+h[j])
    print(h)
    return max(h)


boxes=[
    [2,1,2],
    [3,2,3],
    [2,2,8],
    [2,3,4],
    [2,2,1],
    [4,4,5]
    ]
print(box_stack(boxes))#10 (3 boxes = [2,1,2],[3,2,3],[4,4,5])