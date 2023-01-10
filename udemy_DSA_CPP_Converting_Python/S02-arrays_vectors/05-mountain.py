# dado uma lista de inteiros com alturas, retornar a distancia da maior montanha (distancia entre posicoes inferiores antes e depois)
# ao menos 3 numeros sao requeridos para formar uma montanha (precisa ser anteriormente e posteriormente crescente)

def highest_montain(arr):
    n=len(arr)
    largest=0
    i=1
    while i<n-1:
        if arr[i]>arr[i-1] and arr[i] > arr[i+1]:
            cnt=1
            j=i
            while j>=1 and arr[j]>arr[j-1]:
                j-=1
                cnt+=1
            while i<n-1 and arr[i]>arr[i+1]:
                i+=1
                cnt+=1
            largest=max(largest,cnt)
        else:
            i+=1
    return largest


arr= [5,6,1,2,3,4,5,4,3,2,0,1,2,3,-2,4]
print(highest_montain(arr))