# given an array of size n, find the min # of swaps needed to make the arr as sorted

# precisamos saber posicao correta de cada elemento, para isso, precisamos de sort
# [10,11,5,4,3,2,1] -> neste exemplo, 10->2->11->1 formam um ciclo. Precisamos colocar cada elemento no local correto. (para isso, precisamos n-1 swaps=3)
    # após isso, faltara 5,3 (2-1=1 swap necessario)

def countMinSwaps(a):
    n=len(a)
    ap=[]
    for i,v in enumerate(a):
        ap.append((v,i))
    ap.sort()
    #print(ap)
    visited=[False]*n
    ans=0
    for i in range(n):
        old_pos=ap[i][1]
        if visited[i] or old_pos==i: continue
        node=i
        cycle=0
        while not visited[node]:
            visited[node]=True
            next_node=ap[node][1]
            node=next_node
            cycle+=1
            #print(node)
        ans+=(cycle-1)
    return ans

a1=[5,4,3,2,1] # 2 = (5 e 1 / 4 e 2)
a2=[10,11,5,4,3,2,1] # 4 
print(countMinSwaps(a1))
print(countMinSwaps(a2))