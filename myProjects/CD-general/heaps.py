import heapq
a=[2,3,1,4,9]
heapq.heapify(a) # menor elem sempre na posicao 0
print(a)

heapq.heappush(a,0) # adiciona elem
print(a)

print(heapq.heappop(a)) # removendo menor elem

print(a)
print(heapq.nlargest(3,a)) # 3 maiores elementos do heap
print(heapq.nsmallest(3,a)) # 3 menores elementos do heap