n,m=[int(i) for i in input().split()]
nms=[]
canStart=[[False]*m]*n
finished=[False]*n

for i in range(n):
    nms.append([int(i) for i in input().split()])
    canStart[i][0]=True

time=1
while False in finished:
    for i in range(n):
        for j in range(m):
            if canStart[i][j]:
                pass
    time+=1
