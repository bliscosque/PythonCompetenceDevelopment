#encontrar a maior subarray com a propriedade de que tenha todos os numeros do minimo ao maximo
#Ex: a=[3,7,   1,4,2,5,3,    8,10,9]
#ans=5
nMAX=100

def longConsNumSubA(a):
    ans=0
    n=len(a)
    for l in range(n):
        fr = [False]*nMAX
        nmin=nmax=a[l] # mantem o elem min e max
        for r in range(l,n):
            if fr[a[r]]: break #elem ja existe
            fr[a[r]]=True #add elem
            nmin=min(nmin,a[r])
            nmax=max(nmax,a[r])
            if r-l==nmax-nmin: ans=max(ans,r-l+1) #qnt de elem eh max-min... atualizar resposta
    return ans


a=[3,7,1,4,2,5,3,8,10,9]
print(longConsNumSubA(a))
print(longConsNumSubA([6,1,3,4,5,2,7]))
print(longConsNumSubA([4,1,2,3,7,6]))
print(longConsNumSubA([1,1,1,4,5]))
