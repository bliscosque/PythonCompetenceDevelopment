a=[2,-7,10,3,-1,19,-20,23,17]
global b
b=[0]*len(a)
pSum=[0]*len(a) #parcial sum, inicializado com 0

def update(l,r,val):
    global b
    b[l]+=val
    b[r+1]+=-1*val

update(2,6,5) #da posicao 2 até a posicao 6, incrementar 5
update(3,7,2)
update(1,5,-1)
print(b)
pSum[0]=b[0]
for i in range(1,len(pSum)):
    pSum[i]=pSum[i-1]+b[i]
print(pSum)
c=[a[i]+pSum[i] for i in range(len(a))] #somando as pSum com a
print(c)